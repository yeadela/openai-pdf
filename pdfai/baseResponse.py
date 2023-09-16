import json
from django.http import JsonResponse

class BaseResponse():
    def __init__(self, code, data) -> None:
        self.code = code #1 success, 2 failed
        self.data = data
