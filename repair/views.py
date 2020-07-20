from django.shortcuts import render
from django.views.generic.base import View

from .models import Device


class DeviceView(View):
    def get(self, request):
        device = Device.objects.all()
        return render(request, "repair/device_list.html", {"device_list": device})
