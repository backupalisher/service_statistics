from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from service_statistics import settings
import views.views as mv

urlpatterns = [
    path('', mv.IndexViews.as_view()),
    path('admin/', admin.site.urls),
    path('device_history', include("repair.urls")),
    path('device', include("repair.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
