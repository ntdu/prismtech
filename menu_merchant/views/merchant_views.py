import logging
from django.conf import settings
from rest_framework import permissions, viewsets, status

from core.utils import ApiHelper
from menu_merchant.models import *
from menu_merchant.serializers import *


logger = logging.getLogger()


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = MerchantSerializer


    def list(self, request):
        try:
            limit_req = request.GET.get('limit', 20)
            offset_req = request.GET.get('offset', 1)

            query_set = Merchant.objects.all()
            data_result = ApiHelper.pagination_list_data(
                self.serializer_class(query_set, many=True).data, limit_req, offset_req)

            return ApiHelper.custom_response(200, "Get keywords successfully", data_result)
        except Exception as e:
            logger.exception(f'Get keywords | get exception {e=}')
            return ApiHelper.custom_response(500, str(e))


    def create(self, request, *args, **kwargs):
        if Merchant.objects.filter(owner=request.user).exists():
            return ApiHelper.custom_response(450, "User already have a merchant")

        in_data = request.data
        in_data['owner'] = request.user.id

        serializer = self.serializer_class(data=in_data)
        if serializer.is_valid(raise_exception=True):
            keyword = serializer.save()

        return ApiHelper.custom_response(
            status.HTTP_201_CREATED, "Create keyword successfully", {'id': keyword.id})


    def update(self, request, pk=None):
        pass


    def retrieve(self, request, pk=None):
        pass


    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            merchant = Merchant.objects.filter(id=pk).first()

            if not merchant:
                return ApiHelper.custom_response(450, f'No Merchant with this id: {pk} found')

            merchant.delete()
            return ApiHelper.custom_response(200, 'Delete Merchant successfully')
        except Exception as e:
            logger.exception(f'Delete Merchant | get exception {e=}')
            return ApiHelper.custom_response(500, str(e)) 
