from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class Community(models.Model):
    name = models.CharField(max_length=100)
    user_count = models.IntegerField(default=0)
    payment_status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Free', 'Free')])
    admin_count = models.IntegerField(default=0)
    merchant_count = models.IntegerField(default=0)

class User(AbstractUser):
    ROLE_CHOICES = [('member', 'Member'), ('merchant', 'Merchant'), ('admin', 'Admin')]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    whatsapp = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    
    payment_status = models.CharField(
        max_length=10, 
        choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')]
        )
    deal_metre = models.IntegerField(default=0)
    invited_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )
    
    def __str__(self):
        return self.username
   