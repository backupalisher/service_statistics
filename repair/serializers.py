from django.contrib.auth.models import User, Group
from rest_framework import serializers
from repair.models import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ['name', 'type']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['article', 'serial_number', 'image', 'devices', 'date']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'partcode']


class TypeWorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeWork
        fields = ['name', 'price']


class StatusListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusList
        fields = ['name']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'address', 'date', 'description']


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'status', 'phone', 'address', 'date', 'description', 'client']


class DeviceHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceHistory
        fields = ['articles', 'companies', 'clients', 'type_works', 'products', 'date', 'work_time', 'status',
                  'guarantee', 'description']


class ProductHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductHistory
        fields = ['products', 'companies', 'unit', 'count', 'price', 'date_receipt', 'date_offs', 'description']


class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['products', 'companies', 'unit', 'count', 'price', 'date']
