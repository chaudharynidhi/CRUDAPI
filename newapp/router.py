from newapiapp import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer', viewsets.CustomerViewSets)
