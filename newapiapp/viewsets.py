from rest_framework import viewsets
from .models import EcommerceCustomerData
from .serializer import CustomerSerializer

""" for creating the CRUD API view using ModelViewSet, used this as the implementation is easier for simple CRUD api as compared to AppViewSet """

class CustomerViewSets(viewsets.ModelViewSet):
    queryset = EcommerceCustomerData.objects.all()
    serializer_class = CustomerSerializer


