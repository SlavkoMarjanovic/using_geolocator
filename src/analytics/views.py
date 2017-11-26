from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Oblast, Usersession

class HomePageView(TemplateView):
    template_name = 'index.html'
def county_dataset(request):
    counties = serialize('geojson', Oblast.objects.all())
    return HttpResponse(counties, content_type='json')
def incidentes_dataset(request):
    incidentes = serialize('geojson', Usersession.objects.all())
    return HttpResponse(incidentes, content_type='json')
