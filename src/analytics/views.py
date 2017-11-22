from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Oblast

class HomePageView(TemplateView):
    template_name = 'index.html'
def county_dataset(request):
    counties = serialize('geojson', Oblast.objects.all())
    return HttpResponse(counties, content_type='json')
