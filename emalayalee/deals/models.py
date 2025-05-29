from django.db import models
from merchants.models import MerchantCompany
from users.models import User

class DealsAdd(models.Model):
    STATUS_CHOICES = [('Active', 'Active'), ('Draft', 'Draft'), ('Expired', 'Expired')]
    deal_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    merchant = models.ForeignKey(MerchantCompany, on_delete=models.CASCADE)
    poster = models.TextField()
    category = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()

class DealsUsed(models.Model):
    STATUS_CHOICES = [('Used', 'Used'), ('Not_Used', 'Not_Used')]
    deal = models.ForeignKey(DealsAdd, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    min_purchase_rate = models.DecimalField(max_digits=10, decimal_places=2)
    offer_discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    deal_value = models.DecimalField(max_digits=10, decimal_places=2)

class PurchaseDetails(models.Model):
    deal = models.ForeignKey(DealsAdd, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon = models.CharField(max_length=100)
