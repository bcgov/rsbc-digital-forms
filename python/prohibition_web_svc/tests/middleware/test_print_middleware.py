import asyncio
import base64
from io import BytesIO
import pytest
import json
from unittest.mock import patch, MagicMock
from zipfile import ZipFile
from python.prohibition_web_svc.middleware import print_middleware
from python.common.enums import ErrorCode


class TestPrintMiddleware:
    """Test cases for print middleware functions."""

    def test_log_payload_to_splunk_success(self):
        """Test successful logging of payload to splunk data structure."""
        # Mock request with JSON payload
        mock_request = MagicMock()
        mock_request.get_json.return_value = {
            "template": "test.html",
            "data": {"name": "John Doe", "ssn": "123-45-6789"},
            "options": {"type": "pdf"}
        }
        
        # Mock masked data
        masked_payload = {
            "template": "test.html", 
            "data": {"name": "John Doe", "ssn": "***-**-****"},
            "options": {"type": "pdf"}
        }
        
        with patch('python.prohibition_web_svc.middleware.print_middleware.mv6020_helper.mask_collision_sensitive_data') as mock_mask:
            mock_mask.return_value = masked_payload
            
            kwargs = {
                'request': mock_request,
                'request_id': 'test-request-123',
                'user_guid': 'user-guid-456',
                'username': 'testuser'
            }
            
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            assert result is True
            assert 'splunk_data' in updated_kwargs
            assert updated_kwargs['splunk_data']['event'] == 'print request received'
            assert updated_kwargs['splunk_data']['request_id'] == 'test-request-123'
            assert updated_kwargs['splunk_data']['user_guid'] == 'user-guid-456'
            assert updated_kwargs['splunk_data']['username'] == 'testuser'
            assert updated_kwargs['splunk_data']['payload'] == masked_payload
            
            # Verify mask_collision_sensitive_data was called with the original payload
            mock_mask.assert_called_once()
            called_payload = mock_mask.call_args[0][0]
            assert called_payload['data']['ssn'] == '123-45-6789'

    def test_log_payload_to_splunk_request_exception(self):
        """Test exception handling when request.get_json() fails."""
        # Mock request that raises exception
        mock_request = MagicMock()
        mock_request.get_json.side_effect = Exception("Invalid JSON")
        
        kwargs = {
            'request': mock_request,
            'request_id': 'test-request-123'
        }
        
        with patch('python.prohibition_web_svc.middleware.print_middleware.logger') as mock_logger:
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            assert result is True
            assert 'splunk_data' not in updated_kwargs
            
            # Verify error was logged
            mock_logger.error.assert_called_once()

    def test_log_payload_to_splunk_mask_exception(self):
        """Test exception handling when mask_collision_sensitive_data fails."""
        # Mock request with valid payload
        mock_request = MagicMock()
        mock_request.get_json.return_value = {"template": "test.html", "data": {"name": "John"}}
        
        kwargs = {
            'request': mock_request,
            'request_id': 'test-request-123'
        }
        
        with patch('python.prohibition_web_svc.middleware.print_middleware.mv6020_helper.mask_collision_sensitive_data') as mock_mask:
            mock_mask.side_effect = Exception("Masking failed")
            
            with patch('python.prohibition_web_svc.middleware.print_middleware.logger') as mock_logger:
                result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
                
                assert result is True
                assert 'splunk_data' not in updated_kwargs
                
                # Verify error was logged
                mock_logger.error.assert_called_once()

    def test_log_payload_to_splunk_missing_request(self):
        """Test handling when request is missing from kwargs."""
        kwargs = {
            'request_id': 'test-request-123'
        }
        
        with patch('python.prohibition_web_svc.middleware.print_middleware.logger') as mock_logger:
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            assert result is True
            assert 'splunk_data' not in updated_kwargs
            
            # Verify error was logged
            mock_logger.error.assert_called_once()

    def test_log_payload_to_splunk_empty_kwargs(self):
        """Test handling with completely empty kwargs."""
        kwargs = {}
        
        with patch('python.prohibition_web_svc.middleware.print_middleware.logger') as mock_logger:
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            assert result is True
            assert 'splunk_data' not in updated_kwargs
            
            # Verify error was logged
            mock_logger.error.assert_called_once()

    def test_log_payload_to_splunk_deep_copy(self):
        """Test that payload is deep copied to avoid modifying original."""
        original_payload = {
            "template": "test.html",
            "data": {"name": "John", "nested": {"value": 123}},
            "options": {"type": "pdf"}
        }
        
        mock_request = MagicMock()
        mock_request.get_json.return_value = original_payload
        
        # Mock mask function to modify the payload
        def mock_mask_func(payload):
            # Modify the payload to ensure it's a copy
            payload['data']['nested']['value'] = 999
            return payload
        
        with patch('python.prohibition_web_svc.middleware.print_middleware.mv6020_helper.mask_collision_sensitive_data', side_effect=mock_mask_func):
            kwargs = {'request': mock_request}
            
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            # Original payload should be unchanged
            assert original_payload['data']['nested']['value'] == 123
            
            # But the splunk_data should have the modified value
            assert updated_kwargs['splunk_data']['payload']['data']['nested']['value'] == 999

    def test_log_payload_to_splunk_default_values(self):
        """Test that missing optional fields get default empty string values."""
        mock_request = MagicMock()
        mock_request.get_json.return_value = {"template": "test.html", "data": {"name": "John"}}
        
        with patch('python.prohibition_web_svc.middleware.print_middleware.mv6020_helper.mask_collision_sensitive_data') as mock_mask:
            mock_mask.return_value = {"template": "test.html", "data": {"name": "John"}}
            
            # Test with missing optional fields
            kwargs = {'request': mock_request}
            
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            assert result is True
            splunk_data = updated_kwargs['splunk_data']
            assert splunk_data['request_id'] == ''
            assert splunk_data['user_guid'] == ''
            assert splunk_data['username'] == ''

    def test_update_form_printed_status_success(self):
        """Test successful update of form printed status."""
        payload = {
            "template": "mv6020.html",
            "data": {
                "collision_case_num": "12345",
                "completed_by_id": "user-123"
            }
        }
        kwargs = {
            "payload": payload,
            "user_guid": "default-user"
        }
        
        with patch('python.prohibition_web_svc.middleware.form_middleware.update_form_status') as mock_update, \
             patch('python.prohibition_web_svc.middleware.print_middleware.db.session.commit') as mock_commit:
            
            mock_update.return_value = True
            
            result, updated_kwargs = print_middleware.update_form_printed_status(**kwargs)
            
            assert result is True
            mock_update.assert_called_once()
            # Check arguments passed to update_form_status
            call_args = mock_update.call_args[1]
            assert call_args['form_type'] == 'MV6020'
            assert call_args['form_number'] == '12345'
            assert call_args['user_guid'] == 'user-123'
            assert 'printed_timestamp' in call_args
            
            mock_commit.assert_called_once()

    def test_update_form_printed_status_prefers_form_number(self):
        """Prefer form_number when both form identifiers are provided."""
        payload = {
            "template": "mv6020.html",
            "data": {
                "form_number": "FORM-123",
                "collision_case_num": "COLLISION-456",
            },
        }

        with patch('python.prohibition_web_svc.middleware.form_middleware.update_form_status') as mock_update, \
             patch('python.prohibition_web_svc.middleware.print_middleware.db.session.commit'):
            print_middleware.update_form_printed_status(payload=payload)

        assert mock_update.call_args[1]['form_number'] == 'FORM-123'

    def test_update_form_printed_status_template_not_mapped(self):
        """Test update skipped when template is not mapped."""
        payload = {
            "template": "unknown_template.html",
            "data": {"collision_case_num": "12345"}
        }
        kwargs = {"payload": payload}
        
        with patch('python.prohibition_web_svc.middleware.form_middleware.update_form_status') as mock_update:
            result, updated_kwargs = print_middleware.update_form_printed_status(**kwargs)
            
            assert result is True
            mock_update.assert_not_called()

    def test_update_form_printed_status_no_form_number(self):
        """Test update skipped when no form number is provided."""
        payload = {
            "template": "mv6020.html",
            "data": {"other_field": "value"}
        }
        kwargs = {"payload": payload}
        
        with patch('python.prohibition_web_svc.middleware.form_middleware.update_form_status') as mock_update:
            result, updated_kwargs = print_middleware.update_form_printed_status(**kwargs)
            
            assert result is True
            mock_update.assert_not_called()

    def test_update_form_printed_status_failure(self):
        """Test error handling when update_form_status fails."""
        payload = {
            "template": "mv6020.html",
            "data": {"collision_case_num": "12345"}
        }
        kwargs = {"payload": payload}
        
        with patch('python.prohibition_web_svc.middleware.form_middleware.update_form_status') as mock_update:
            mock_update.return_value = False
            
            result, updated_kwargs = print_middleware.update_form_printed_status(**kwargs)
            
            assert result is True
            assert 'error' not in updated_kwargs
            
    def test_update_form_printed_status_exception(self):
        """Test exception handling in update_form_printed_status."""
        kwargs = {} # Missing payload will raise KeyError or similar
        
        result, updated_kwargs = print_middleware.update_form_printed_status(**kwargs)
        
        assert result is True
        assert 'error' in updated_kwargs
        assert updated_kwargs['error']['error_code'] == ErrorCode.P02

    def test_render_document_with_playwright_all_zip_decodes_pdf_attachments(self, monkeypatch):
        """Test that download-all zip output contains decoded PDF bytes, not base64 text."""
        payload = {
            "template": "mv6020.html",
            "options": {"type": "pdf"},
            "data": {
                "collision_case_num": "AB123",
                "police_file_num": "PF-77",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "print_options": {"type": "all"},
                "entities": [],
            },
        }

        pdf_bytes = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog >>\nendobj\n"
        encoded_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

        monkeypatch.setattr(
            print_middleware.mv6020_helper,
            "generate_all_PDF_attachments",
            lambda **kw: (
                True,
                {
                    **kw,
                    "attachments": [
                        {
                            "content": encoded_pdf,
                            "contentType": "application/pdf",
                            "encoding": "base64",
                            "filename": "MV6020-AB123-police-copy.pdf",
                        }
                    ],
                },
            ),
        )

        success, result = print_middleware.render_document_with_playwright(payload=payload)

        assert success is True
        assert result["content_type"] == "application/zip"
        assert result["filename"] == "MV6020_AB123_PF-77_20251120_All_PDF.zip"
        zip_bytes = result["rendered_content"]
        with ZipFile(BytesIO(zip_bytes), "r") as zip_file:
            names = zip_file.namelist()
            assert names == ["MV6020-AB123-police-copy.pdf"]
            extracted = zip_file.read(names[0])

        assert extracted == pdf_bytes


class _FakePage:
    def __init__(self, tracker):
        self.tracker = tracker
        self.html = None

    async def set_content(self, html, wait_until=None):
        self.html = html

    async def evaluate(self, script):
        return None

    async def content(self):
        return self.html

    async def pdf(self, **kwargs):
        self.tracker["active"] += 1
        self.tracker["max_active"] = max(self.tracker["max_active"], self.tracker["active"])
        await asyncio.sleep(0.01)
        self.tracker["active"] -= 1
        if "FAIL" in self.html:
            raise RuntimeError("pdf failed")
        return b"PDF:" + self.html.encode()


class _FakeContext:
    def __init__(self, tracker):
        self.tracker = tracker

    async def new_page(self):
        return _FakePage(self.tracker)

    async def close(self):
        self.tracker["contexts_closed"] += 1


class _FakeBrowser:
    def __init__(self, tracker):
        self.tracker = tracker

    async def new_context(self, **kwargs):
        return _FakeContext(self.tracker)

    async def close(self):
        self.tracker["browsers_closed"] += 1


class _FakePlaywright:
    def __init__(self, tracker):
        self.chromium = self
        self.tracker = tracker

    async def launch(self, **kwargs):
        self.tracker["launches"] += 1
        return _FakeBrowser(self.tracker)


def _fake_async_playwright(tracker):
    class _CM:
        async def __aenter__(self):
            return _FakePlaywright(tracker)

        async def __aexit__(self, *exc):
            return False

    return lambda: _CM()


@pytest.fixture
def tracker(monkeypatch):
    t = {"launches": 0, "browsers_closed": 0, "contexts_closed": 0, "active": 0, "max_active": 0}
    monkeypatch.setattr(print_middleware, "async_playwright", _fake_async_playwright(t))
    return t


@pytest.fixture
def template_file(tmp_path):
    (tmp_path / "logo.png").write_bytes(b"\x89PNG-fake")
    tpl = tmp_path / "t.html"
    tpl.write_text(
        '<html><body><img src="logo.png"><img src="https://x/y.png">'
        "<p>{{ data.name }}</p></body></html>"
    )
    return str(tpl)


def _data(name="A"):
    return {"name": name, "form_details": {"form_no": "1", "form_title": "T", "subtext": "s", "form_version": "v"}}


class TestImageDataUrl:
    def test_existing_image_returns_data_url(self, tmp_path):
        print_middleware._image_data_url.cache_clear()
        img = tmp_path / "a.jpg"
        img.write_bytes(b"abc")
        url = print_middleware._image_data_url(str(img))
        assert url == "data:image/jpeg;base64," + base64.b64encode(b"abc").decode()

    def test_unknown_extension_defaults_to_png(self, tmp_path):
        print_middleware._image_data_url.cache_clear()
        img = tmp_path / "a.bin"
        img.write_bytes(b"abc")
        assert print_middleware._image_data_url(str(img)).startswith("data:image/png;base64,")

    def test_missing_image_returns_none(self, tmp_path):
        print_middleware._image_data_url.cache_clear()
        assert print_middleware._image_data_url(str(tmp_path / "nope.png")) is None

    def test_result_is_cached(self, tmp_path):
        print_middleware._image_data_url.cache_clear()
        img = tmp_path / "a.png"
        img.write_bytes(b"abc")
        print_middleware._image_data_url(str(img))
        print_middleware._image_data_url(str(img))
        assert print_middleware._image_data_url.cache_info().hits == 1


class TestBuildHtml:
    def test_inlines_relative_images_only(self, template_file):
        print_middleware._image_data_url.cache_clear()
        html, template_data = print_middleware._build_html(template_file, _data("Bob"), "pdf")
        assert 'src="data:image/png;base64,' in html
        assert 'src="https://x/y.png"' in html
        assert "<p>Bob</p>" in html
        assert template_data["output_type"] == "pdf"

    def test_missing_relative_image_left_unchanged(self, tmp_path):
        tpl = tmp_path / "t.html"
        tpl.write_text('<img src="missing.png">')
        html, _ = print_middleware._build_html(str(tpl), {}, "pdf")
        assert 'src="missing.png"' in html


class TestRenderMany:
    def test_single_browser_launch_and_ordered_results(self, tracker, template_file):
        data_list = [_data(f"n{i}") for i in range(5)]
        results = print_middleware.render_many_with_playwright(template_file, data_list, "pdf")

        assert tracker["launches"] == 1
        assert tracker["browsers_closed"] == 1
        assert tracker["contexts_closed"] == 5
        assert all(ok for ok, _ in results)
        for i, (_, content) in enumerate(results):
            assert content.startswith(b"PDF:") and f"n{i}".encode() in content

    def test_concurrency_is_capped(self, tracker, template_file, monkeypatch):
        monkeypatch.setattr(print_middleware, "MAX_CONCURRENT_RENDERS", 2)
        print_middleware.render_many_with_playwright(template_file, [_data(f"n{i}") for i in range(6)], "pdf")
        assert 1 < tracker["max_active"] <= 2

    def test_one_failure_does_not_affect_others(self, tracker, template_file):
        results = print_middleware.render_many_with_playwright(
            template_file, [_data("ok1"), _data("FAIL"), _data("ok2")], "pdf"
        )
        assert [ok for ok, _ in results] == [True, False, True]
        assert "pdf failed" in results[1][1]
        assert tracker["contexts_closed"] == 3

    def test_html_output_type(self, tracker, template_file):
        results = print_middleware.render_many_with_playwright(template_file, [_data("h")], "html")
        assert results[0][0] is True
        assert "<p>h</p>" in results[0][1]

    def test_template_error_fails_all_jobs(self, tracker, tmp_path):
        results = print_middleware.render_many_with_playwright(str(tmp_path / "missing.html"), [{}, {}], "pdf")
        assert [ok for ok, _ in results] == [False, False]
        assert tracker["launches"] == 0

    def test_single_render_wrapper(self, tracker, template_file):
        success, content = print_middleware.render_with_playwright(template_file, _data("solo"), "pdf")
        assert success is True
        assert b"solo" in content
        assert tracker["launches"] == 1


class TestChangeReportPrint:
    """Previews and downloads of a change report highlight what changed since the parent."""

    PARENT = {'collision_case_num': 'RZ001036', 'street_on': 'MAIN ST', 'entities': []}

    def _payload(self, ptype='police', **changes):
        data = dict(self.PARENT, isChangeReport=True, parentRevision=2, print_options={'type': ptype}, **changes)
        return {'template': 'mv6020.html', 'data': data, 'parentData': dict(self.PARENT)}

    @pytest.mark.parametrize('ptype', ['police', 'icbc', 'entity', 'all'])
    def test_every_copy_gets_the_highlights(self, ptype):
        payload = self._payload(ptype, street_on='1ST AVE')
        result, kwargs = print_middleware.add_change_report_context(payload=payload)
        assert result is True
        context = kwargs['payload']['data']['change_report']
        assert context['highlights_available'] is True
        assert context['changed'] == ['street_on']
        assert context['revision'] == 3

    @pytest.mark.parametrize('ptype, highlighted', [('police', True), ('icbc', True), ('ICBC', True),
                                                    ('entity', False), (None, False)])
    def test_only_police_and_icbc_copies_show_the_changes(self, ptype, highlighted):
        payload = self._payload(ptype, street_on='1ST AVE')
        result, kwargs = print_middleware.add_change_report_context(payload=payload)
        template_data = print_middleware.change_report_helper.context_for_copy(kwargs['payload']['data'])
        assert ('change_report' in template_data) is highlighted
        assert 'change_report' in kwargs['payload']['data']  # still there for the next copy of a zip

    def test_download_all_highlights_the_police_copy_but_not_the_driver_copies(self):
        payload = self._payload('all', street_on='1ST AVE',
                                entities=[{'entity_num': 1}, {'entity_num': 2}],
                                police_file_num='P1', date_collision='2025-11-20T00:00:00-08:00')
        payload['parentData']['entities'] = [{'entity_num': 1}, {'entity_num': 2}]
        payload['options'] = {'type': 'pdf'}
        _, kwargs = print_middleware.add_change_report_context(payload=payload)
        seen = []

        def render_many(template_path, data_list, output_type='pdf'):
            for data in data_list:
                template_data = print_middleware.change_report_helper.context_for_copy(dict(data))
                seen.append((data['print_options']['type'], 'change_report' in template_data))
            return [(True, b'%PDF') for _ in data_list]

        with patch.object(print_middleware, 'render_many_with_playwright', side_effect=render_many):
            result, kwargs = print_middleware.render_document_with_playwright(**kwargs)
        assert result is True
        assert seen == [('police', True), ('entity', False), ('entity', False)]

    @pytest.mark.parametrize('ptype, shown', [('police', 'highlighted'), ('icbc', 'highlighted'), ('entity', 'plain')])
    def test_every_render_passes_through_the_per_copy_context(self, tmp_path, ptype, shown):
        template = tmp_path / 'probe.html'
        template.write_text("{{ 'highlighted' if data.change_report else 'plain' }}")
        _, kwargs = print_middleware.add_change_report_context(payload=self._payload(ptype, street_on='1ST AVE'))
        html, _ = print_middleware._build_html(str(template), kwargs['payload']['data'], 'html')
        assert html == shown

    def test_parent_data_is_not_passed_to_the_template(self):
        result, kwargs = print_middleware.add_change_report_context(payload=self._payload())
        assert 'parentData' not in kwargs['payload']

    def test_missing_parent_prints_without_highlights(self):
        payload = self._payload(street_on='1ST AVE')
        del payload['parentData']
        result, kwargs = print_middleware.add_change_report_context(payload=payload)
        assert result is True
        assert kwargs['payload']['data']['change_report']['highlights_available'] is False

    def test_new_reports_are_unchanged(self):
        payload = {'template': 'mv6020.html', 'data': dict(self.PARENT, print_options={'type': 'police'})}
        result, kwargs = print_middleware.add_change_report_context(payload=payload)
        assert result is True
        assert 'change_report' not in kwargs['payload']['data']

    def test_a_failure_never_stops_the_print(self):
        with patch.object(print_middleware.change_report_helper, 'build_context', side_effect=ValueError('boom')):
            result, kwargs = print_middleware.add_change_report_context(payload=self._payload())
        assert result is True
        assert 'change_report' not in kwargs['payload']['data']

    def test_parent_data_is_masked_in_the_splunk_log(self):
        request = MagicMock()
        request.get_json.return_value = {
            'template': 'mv6020.html',
            'data': {'entities': [{'surname': 'CURRENT'}]},
            'parentData': {'entities': [{'surname': 'PARENT', 'involved_persons': [{'given_name': 'P'}]}]},
        }
        result, kwargs = print_middleware.log_payload_to_splunk(request=request)
        logged = json.dumps(kwargs['splunk_data'])
        assert 'PARENT' not in logged and 'CURRENT' not in logged and '"P"' not in logged
