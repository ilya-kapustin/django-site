from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from ..models import ShopsGroup, Shops


class ShopsGroupSerializer(serializers.ModelSerializer):
    '''
    Данные, отправленные в serializers:
    name, description.
    В классе Meta указываю использываемую модель, а также поля
    '''
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = ShopsGroup
        fields = ['name', 'description', 'pk']


class ShopsSerializer(serializers.ModelSerializer):
    '''
    Данные, отправленные в serializers:
    title, code_thing, img, description, price, views_count, group.
    В классе Meta указываю использываемую модель, а также все поля
    '''
    title = serializers.CharField(required=True)
    code_thing = serializers.IntegerField(required=True)
    img = serializers.ImageField(required=True)
    description = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    views_count = serializers.IntegerField(required=True)
    group = serializers.PrimaryKeyRelatedField(queryset=ShopsGroup)

    class Meta:
        model = Shops
        fields = '__all__'
