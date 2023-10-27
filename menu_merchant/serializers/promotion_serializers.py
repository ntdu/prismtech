from menu_merchant.models import Promotion
from rest_framework import serializers


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'
