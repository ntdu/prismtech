from typing import Any, Dict

from rest_framework import status
from rest_framework.response import Response

class ApiHelper:
    @staticmethod
    def pagination_list_data(data, limit = 10, offset = 1):
        data_result = {
            'count': len(data),
            'data': []
        }

        if data:
            _end = int(offset) * int(limit)
            _start = int(_end) - int(limit)
            data_result.update({'data': data[_start:_end]})

        return data_result

    @staticmethod
    def custom_response(status_code=status.HTTP_200_OK, message='', data=[]):
        return Response(
            {
                "status": status_code,
                "message": message,
                "data": data
            },
            status=status_code
        )