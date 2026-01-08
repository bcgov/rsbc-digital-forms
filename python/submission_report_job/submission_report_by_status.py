
class SubmissionReportByStatus():
    form_name: str
    items: list['SubmissionReportByStatusItem']
    total_count: int

    def __init__(self, form_name: str):
        self.form_name = form_name
        self.items = []
        self.total_count = 0

class SubmissionReportByStatusItem():    
    application_status: str
    offline: bool
    count: int

    def __init__(self, application_status: str, offline: bool, count: int):
        self.application_status = application_status
        self.offline = offline
        self.count = count
