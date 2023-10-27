from menu_merchant.models import Merchant
from rest_framework import serializers


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
