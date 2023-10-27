import logging
from rest_framework import permissions, viewsets, status

from core.utils import ApiHelper
from menu_merchant.models import *
from menu_merchant.serializers import *


logger = logging.getLogger()


class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = HashtagSerializer


    def list(self, request):
        try:
            limit_req = request.GET.get('limit', 20)
            offset_req = request.GET.get('offset', 1)

            query_set = Hashtag.objects.all()
            data_result = ApiHelper.pagination_list_data(
                self.serializer_class(query_set, many=True).data, limit_req, offset_req)

            return ApiHelper.custom_response(200, "Get hashtags successfully", data_result)
        except Exception as e:
            logger.exception(f'Get hashtags | get exception {e=}')
            return ApiHelper.custom_response(500, str(e))


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            hashtag = serializer.save()

        return ApiHelper.custom_response(
            status.HTTP_201_CREATED, "Create hashtag successfully", {'id': hashtag.id})


    def update(self, request, pk=None):
        pass


    def retrieve(self, request, pk=None):
        pass


    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            hashtag = Hashtag.objects.filter(id=pk).first()

            if not hashtag:
                return ApiHelper.custom_response(411, f'No Hashtag with this id: {pk} found')

            hashtag.delete()
            return ApiHelper.custom_response(200, 'Delete Hashtag successfully')
        except Exception as e:
            logger.exception(f'Delete Keyword | get exception {e=}')
            return ApiHelper.custom_response(500, str(e)) 
