# Create your views here.
from django.shortcuts import render
from repair.models import DeviceHistory
from django.views.generic.base import TemplateView


# Create your views here.
# def index(request):
    # device_history = DeviceHistory.get_context
    # return render(request, 'index.html', context={"device_history": device_history})


class IndexViews(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexViews, self).get_context_data(**kwargs)
        context['device_history'] = DeviceHistory.objects.all()
        return context
