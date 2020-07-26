from rest_framework import viewsets, generics, views, status
from django.contrib.auth import authenticate
# ViewSets define the view behavior.
from rest_framework.response import Response

from repair.serializers import *


class LoginView(views.APIView):
    permission_classes = ()

    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TypeWorkViewSet(viewsets.ModelViewSet):
    queryset = TypeWork.objects.all()
    serializer_class = TypeWorkSerializer


class StatusListViewSet(viewsets.ModelViewSet):
    queryset = StatusList.objects.all()
    serializer_class = StatusListSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DeviceHistoryViewSet(viewsets.ModelViewSet):
    queryset = DeviceHistory.objects.all()
    serializer_class = DeviceHistorySerializer


class ProductHistoryViewSet(viewsets.ModelViewSet):
    queryset = ProductHistory.objects.all()
    serializer_class = ProductHistorySerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
