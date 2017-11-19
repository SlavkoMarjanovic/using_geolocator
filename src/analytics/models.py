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


