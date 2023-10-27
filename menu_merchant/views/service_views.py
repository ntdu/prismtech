import logging
from rest_framework import permissions, viewsets, status

from core.utils import ApiHelper
from menu_merchant.models import *
from menu_merchant.serializers import *


logger = logging.getLogger()


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ServiceSerializer


    def list(self, request):
        try:
            limit_req = request.GET.get('limit', 20)
            offset_req = request.GET.get('offset', 1)

            query_set = Service.objects.all()
            data_result = ApiHelper.pagination_list_data(
                self.serializer_class(query_set, many=True).data, limit_req, offset_req)

            return ApiHelper.custom_response(200, "Get services successfully", data_result)
        except Exception as e:
            logger.exception(f'Get services | get exception {e=}')
            return ApiHelper.custom_response(500, str(e))


    def create(self, request, *args, **kwargs):
        in_data = request.data
        in_data['owner'] = request.user.id

        serializer = self.serializer_class(data=in_data)
        if serializer.is_valid(raise_exception=True):
            service = serializer.save()

        return ApiHelper.custom_response(
            status.HTTP_201_CREATED, "Create service successfully", {'id': service.id})


    def update(self, request, pk=None):
        pass


    def retrieve(self, request, pk=None):
        pass


    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            service = Service.objects.filter(id=pk).first()

            if not service:
                return ApiHelper.custom_response(411, f'No Service with this id: {pk} found')

            service.delete()
            return ApiHelper.custom_response(200, 'Delete Service successfully')
        except Exception as e:
            logger.exception(f'Delete Service | get exception {e=}')
            return ApiHelper.custom_response(500, str(e)) 
