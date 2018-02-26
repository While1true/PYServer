from Vange.models import Bug

BASE_MODEL='''{{"message":"成功","data":{data},"code":200}}'''
from datetime import datetime
import json

import json
from datetime import date, datetime
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