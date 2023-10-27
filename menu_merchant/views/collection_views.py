import logging
from rest_framework import permissions, viewsets, status

from core.utils import ApiHelper
from menu_merchant.models import *
from menu_merchant.serializers import *


logger = logging.getLogger()


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CollectionSerializer


    def list(self, request):
        try:
            limit_req = request.GET.get('limit', 20)
            offset_req = request.GET.get('offset', 1)

            query_set = Collection.objects.all()
            data_result = ApiHelper.pagination_list_data(
                self.serializer_class(query_set, many=True).data, limit_req, offset_req)

            return ApiHelper.custom_response(200, "Get collections successfully", data_result)
        except Exception as e:
            logger.exception(f'Get collections | get exception {e=}')
            return ApiHelper.custom_response(500, str(e))


    def create(self, request, *args, **kwargs):
        in_data = request.data
        in_data['owner'] = request.user.id

        serializer = self.serializer_class(data=in_data)
        if serializer.is_valid(raise_exception=True):
            collection = serializer.save()

        return ApiHelper.custom_response(
            status.HTTP_201_CREATED, "Create collection successfully", {'id': collection.id})


    def update(self, request, pk=None):
        pass


    def retrieve(self, request, pk=None):
        pass


    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            collection = Collection.objects.filter(id=pk).first()

            if not collection:
                return ApiHelper.custom_response(411, f'No collection with this id: {pk} found')

            collection.delete()
            return ApiHelper.custom_response(200, 'Delete collection successfully')
        except Exception as e:
            logger.exception(f'Delete collection | get exception {e=}')
            return ApiHelper.custom_response(500, str(e)) 
