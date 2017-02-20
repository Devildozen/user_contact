from xml.dom.minidom import _set_attribute_node

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'id'

    username = None
    email = None
    contact = models.OneToOneField('Contact', on_delete=models.CASCADE)

    def get_username(self):
        return str(getattr(self, self.USERNAME_FIELD))


class Contact(models.Model):

    AUTH_FIELDS = ['email', 'phone_number']

    username = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
