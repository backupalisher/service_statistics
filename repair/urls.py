from django.urls import path

from . import views


urlpatterns = [
    path("", views.DeviceView.as_view())
]
