from rest_framework import serializers
from .models import EcommerceCustomerData

#used serializers to convert the complex model instances to native Python datatypes and those can be easily rendered into JSON

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceCustomerData
        fields = "__all__"
