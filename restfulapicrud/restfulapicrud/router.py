from employeeapi.viewsets import employeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', employeeViewSet)
