from newapiapp import viewsets
from rest_framework import routers
# Rest Framework adds support for automatic URL routing to django and provides with simple way of writing the viewsets.
router = routers.DefaultRouter()
router.register('customer', viewsets.CustomerViewSets)
