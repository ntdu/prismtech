import logging
from rest_framework import permissions, viewsets, status

from core.utils import ApiHelper
from menu_merchant.models import *
from menu_merchant.serializers import *


logger = logging.getLogger()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CategorySerializer


    def list(self, request):
        limit_req = request.GET.get('limit', 20)
        offset_req = request.GET.get('offset', 1)

        query_set = Category.objects.all()
        data_result = ApiHelper.pagination_list_data(
            self.serializer_class(query_set, many=True).data, limit_req, offset_req)

        return ApiHelper.custom_response(200, "Get category successfully", data_result)


    def create(self, request, *args, **kwargs):
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
        category = Category.objects.filter(id=pk).first()

        if not category:
            return ApiHelper.custom_response(411, f'No Category with this id: {pk} found')

        category.delete()
        return ApiHelper.custom_response(200, 'Delete Category successfully')
