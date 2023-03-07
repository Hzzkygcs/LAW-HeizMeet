import json

from django.http import HttpResponseBase, HttpResponse


class AutomaticallyHandledException(Exception):
    def __init__(self, status_code: int, message):
        super(Exception, self).__init__(message)
        self.status_code = status_code
        self.err_msg = message
        self.http_response_class = HttpResponse

    def get_response(self, req) -> HttpResponseBase:
        data = json.dumps({
            'status_code': self.status_code,
            'err_msg': self.err_msg,
        })
        return self.http_response_class(data, content_type="application/json")