from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import views.views as mv
from repair.view_sets import *
from service_statistics import settings

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'products', ProductViewSet)
router.register(r'type_works', TypeWorkViewSet)
router.register(r'status_list', StatusListViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'device_histories', DeviceHistoryViewSet)
router.register(r'product_histories', ProductHistoryViewSet)
router.register(r'warehouse', WarehouseViewSet)

urlpatterns = [
    path('', mv.IndexViews.as_view()),
    path('admin/', admin.site.urls),
    path('device_history', include("repair.urls")),
    path('device', include("repair.urls")),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
