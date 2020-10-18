from django.db import models

# Create your models here.
class EcommerceCustomerData(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=250, default='Unnamed Substance')
    brand_name = models.CharField(max_length=250, default='Not Available')
    regular_price_value = models.FloatField(default=0)
    offer_price_value = models.FloatField(default=0)
    currency = models.CharField(max_length=50, default='GBP')
    classification_l1 = models.CharField(max_length=250, blank=True)
    classification_l2 = models.CharField(max_length=250, blank=True)
    classification_l3 = models.CharField(max_length=250, blank=True)
    classification_l4 = models.CharField(max_length=250, blank=True)
    image_url = models.URLField(max_length = 250, default='Not Available') 


#Create/Insert
