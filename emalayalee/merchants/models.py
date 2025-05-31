from django.db import models
from users.models import User
from django.conf import settings

class MerchantCompany(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    tax_invoice_no = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

class MerchantRequest(models.Model):
    STATUS_CHOICES = [('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')]
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'admin'},
        related_name='merchant_requests'
    )
    merchant = models.ForeignKey(MerchantCompany, on_delete=models.CASCADE)
    accept_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    requested_time = models.DateTimeField(auto_now_add=True)
