from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from repair.models import *


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email',  'password', 'is_staff', 'groups']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


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
