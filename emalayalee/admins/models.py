from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=100)
    invitation = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
