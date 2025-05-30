from django.db import models

# Create your models here.

class Community(models.Model):
    name = models.CharField(max_length=100)
    user_count = models.IntegerField(default=0)
    payment_status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Free', 'Free')])
    admin_count = models.IntegerField(default=0)
    merchant_count = models.IntegerField(default=0)

class User(models.Model):
    ROLE_CHOICES = [('member', 'Member'), ('merchant', 'Merchant'), ('admin', 'Admin')]
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    whatsapp = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    payment_status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    deal_metre = models.IntegerField(default=0)
    def __str__(self):
        return self.username
   