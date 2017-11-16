from django.db import models
from django.conf import settings
from .signal import user_logged_in

class UserSession(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL)
    session_key     = models.CharField(max_length=60, blank=True, null=True)
    ip_address      = models.GenericIPAddressField(blank=True, null=True)
    city_data       = models.TextField(blank=True, null=True)
    city            = models.CharField(max_length=120, blank=True, null=True)
    country         = models.CharField(max_length=120, blank=True, null=True)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.city_data:
            return str(self.city_data)
        else:
            return self.user.username
def user_logged_in_receiver(sender, request, *args, **kwargs):
    user = sender

user_logged_in.connect(user_logged_in_receiver)

