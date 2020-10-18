from rest_framework import serializers
from .models import EcommerceCustomerData

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceCustomerData
        fields = "__all__"