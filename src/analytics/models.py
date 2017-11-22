from django.db import models
from django.conf import settings
from .signal import user_logged_in
from django.contrib.gis.db import models

class Usersession(models.Model):

    name            = models.CharField(max_length=20, blank=True, null=True)
    location        = models.PointField(srid=4326)
    objects         = models.GeoManager()

    def __str__(self):
        if self.name:
            return str(self.name)
        else:
            return self.name

class Oblast(models.Model):
    id_0 = models.IntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=75)
    hasc_1 = models.CharField(max_length=15)
    ccn_1 = models.IntegerField()
    cca_1 = models.CharField(max_length=254)
    type_1 = models.CharField(max_length=50)
    engtype_1 = models.CharField(max_length=50)
    nl_name_1 = models.CharField(max_length=50)
    varname_1 = models.CharField(max_length=150)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.name_0


