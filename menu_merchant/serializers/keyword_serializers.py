from menu_merchant.models import Keyword
from rest_framework import serializers


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'
