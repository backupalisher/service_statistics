from django.contrib import admin
from .models import Device, Article, Company, Client, Product, DeviceHistory, ProductHistory, TypeWork, Warehouse, \
    StatusList

models_list = [Device, Article, Company, Client, DeviceHistory, Product, ProductHistory, TypeWork, Warehouse,
               StatusList]

admin.site.register(models_list)
