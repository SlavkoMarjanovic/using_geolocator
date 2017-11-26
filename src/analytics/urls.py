from .views import HomePageView, county_dataset, incidentes_dataset
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^county_data/$', county_dataset, name='county'),
    url(r'^incidence_data$', incidentes_dataset, name='incidences'),
]
