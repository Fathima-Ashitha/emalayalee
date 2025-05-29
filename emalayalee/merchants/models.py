from django.db import models
from users.models import User

class MerchantCompany(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    tax_invoice_no = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

class MerchantRequest(models.Model):
    STATUS_CHOICES = [('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')]
    admin = models.ForeignKey('admins.Admin', on_delete=models.CASCADE)
    merchant = models.ForeignKey(MerchantCompany, on_delete=models.CASCADE)
    accept_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    requested_time = models.DateTimeField(auto_now_add=True)
