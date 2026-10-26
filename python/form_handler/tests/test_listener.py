from types import SimpleNamespace
from unittest.mock import Mock, call

import pytest

from python.form_handler import listener as listener_module
from python.form_handler.listener import Listener
from python.form_handler.rabbitmq import RabbitMQ


def test_main_registers_storage_and_offline_queues():
    rabbit_listener = Mock()
    rabbit_listener.consume_queues.side_effect = RuntimeError("stop")
    config = SimpleNamespace(
        STORAGE_WATCH_QUEUE="storage-events",
        OFFLINE_SUBMISSION_WATCH_QUEUE="offline-submissions",
    )
    listener = Listener(config, Mock(), rabbit_listener)

    with pytest.raises(RuntimeError, match="stop"):
        listener.main()

    queues = rabbit_listener.consume_queues.call_args.args[0]
    assert queues == {
        "storage-events": listener.callback,
        "offline-submissions": listener.offline_submission_callback,
    }


def test_offline_submission_callback_runs_business_pipeline(monkeypatch):
    message = {"id": 42}
    pipeline = [{"try": Mock(), "fail": []}]
    monkeypatch.setattr(listener_module, "decode_message", Mock(return_value=message))
    process_pipeline = Mock(return_value=pipeline)
    middle_logic = Mock()
    monkeypatch.setattr(
        listener_module.business,
        "process_incoming_offline_submissions",
        process_pipeline,
    )
    monkeypatch.setattr(listener_module.helper, "middle_logic", middle_logic)

    config = SimpleNamespace(
        ENCRYPT_KEY="key",
        OFFLINE_SUBMISSION_MAX_RETRIES=5,
        OFFLINE_SUBMISSION_HOLD_QUEUE="offline-hold",
        OFFLINE_SUBMISSION_FAIL_QUEUE="offline-fail",
    )
    writer = Mock()
    writer.publish_confirmed.return_value = True
    callback = Listener(config, writer, Mock()).offline_submission_callback
    channel = Mock()
    method = SimpleNamespace(delivery_tag=7)

    callback(channel, method, None, b"message")

    process_pipeline.assert_called_once_with()
    middle_logic.assert_called_once_with(
        pipeline,
        message=message,
        config=config,
        writer=writer,
        app=listener_module.application,
        db=listener_module.db,
    )
    channel.basic_ack.assert_called_once_with(delivery_tag=7)


def test_offline_submission_callback_requeues_unexpected_pipeline_exception(monkeypatch):
    monkeypatch.setattr(listener_module, "decode_message", Mock(return_value={"id": 42}))
    monkeypatch.setattr(listener_module.helper, "middle_logic", Mock(side_effect=RuntimeError("failure")))
    config = SimpleNamespace(
        ENCRYPT_KEY="key",
        OFFLINE_SUBMISSION_MAX_RETRIES=5,
        OFFLINE_SUBMISSION_HOLD_QUEUE="offline-hold",
        OFFLINE_SUBMISSION_FAIL_QUEUE="offline-fail",
    )
    writer = Mock()
    callback = Listener(config, writer, Mock()).offline_submission_callback
    channel = Mock()
    method = SimpleNamespace(delivery_tag=8)

    callback(channel, method, None, b"message")

    channel.basic_nack.assert_called_once_with(delivery_tag=8, requeue=True)
    channel.basic_ack.assert_not_called()
    writer.publish_confirmed.assert_not_called()


def test_offline_submission_callback_requeues_decode_exception(monkeypatch):
    monkeypatch.setattr(
        listener_module,
        "decode_message",
        Mock(side_effect=ValueError("invalid message")),
    )
    config = SimpleNamespace(
        ENCRYPT_KEY="key",
        OFFLINE_SUBMISSION_MAX_RETRIES=2,
        OFFLINE_SUBMISSION_HOLD_QUEUE="offline-hold",
        OFFLINE_SUBMISSION_FAIL_QUEUE="offline-fail",
    )
    writer = Mock()
    callback = Listener(config, writer, Mock()).offline_submission_callback
    channel = Mock()
    method = SimpleNamespace(delivery_tag=9)

    callback(channel, method, None, b"invalid")

    channel.basic_nack.assert_called_once_with(delivery_tag=9, requeue=True)
    channel.basic_ack.assert_not_called()
    writer.publish_confirmed.assert_not_called()


def test_consume_queues_registers_all_callbacks_before_consuming():
    rabbit = object.__new__(RabbitMQ)
    rabbit.channel = Mock()
    rabbit._verify_or_create = Mock()
    storage_callback = Mock()
    offline_callback = Mock()

    RabbitMQ.consume_queues(
        rabbit,
        {"storage-events": storage_callback, "offline-submissions": offline_callback},
    )

    assert rabbit.channel.basic_consume.call_args_list == [
        call(queue="storage-events", on_message_callback=storage_callback),
        call(queue="offline-submissions", on_message_callback=offline_callback),
    ]
    rabbit.channel.start_consuming.assert_called_once_with()


def test_publish_confirmed_accepts_none_return_from_basic_publish():
    rabbit = object.__new__(RabbitMQ)
    rabbit.channel = Mock()
    rabbit.channel.basic_publish.return_value = None
    rabbit._refresh_connection = Mock()

    assert rabbit.publish_confirmed("offline-hold", b"payload") is True

    rabbit.channel.confirm_delivery.assert_called_once_with()
    rabbit.channel.basic_publish.assert_called_once()


def test_publish_confirmed_returns_false_after_publish_errors():
    rabbit = object.__new__(RabbitMQ)
    rabbit.channel = Mock()
    rabbit.channel.basic_publish.side_effect = RuntimeError("broker rejected publish")
    rabbit._refresh_connection = Mock()

    assert rabbit.publish_confirmed("offline-hold", b"payload") is False


def test_publish_confirmed_treats_non_raising_none_as_success():
    rabbit = object.__new__(RabbitMQ)
    rabbit.channel = Mock()
    rabbit.channel.basic_publish.return_value = None
    rabbit._refresh_connection = Mock()

    result = rabbit.publish_confirmed("offline-hold", b"payload")

    assert result is True
    rabbit.channel.confirm_delivery.assert_called_once_with()
    rabbit.channel.basic_publish.assert_called_once()