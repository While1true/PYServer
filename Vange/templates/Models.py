from Vange.models import Bug

from datetime import datetime
import json

import json
from datetime import date, datetime
from django.db.models import QuerySet


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        # if isinstance(obj, datetime.datetime):
        #     return int(mktime(obj.timetuple()))
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class JsonResult(object):
    BASE_MODEL = '''{{"message":{message},"data":{data},"code":{code}}}'''

    @staticmethod
    def success(data) -> str:
        if isinstance(data, QuerySet):
            data = json.dumps(list(data), cls=DateEncoder)
        elif isinstance(data, dict) or isinstance(data, list):
            data = json.dumps(data)
        return JsonResult.BASE_MODEL.format(message='"success"', code=200, data=data)

    @staticmethod
    def failure(message) -> str:
        return JsonResult.BASE_MODEL.format(message=message, code=100, data=None)
