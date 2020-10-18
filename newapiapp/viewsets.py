from rest_framework import viewsets
from .models import EcommerceCustomerData
from .serializer import CustomerSerializer

class CustomerViewSets(viewsets.ModelViewSet):
    queryset = EcommerceCustomerData.objects.all()
    serializer_class = CustomerSerializer


