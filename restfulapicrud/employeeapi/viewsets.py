from rest_framework import viewsets
from . import models
from . import serializers
# Viewset enable the exposure of CRUD operation.
class employeeViewSet(viewsets.ModelViewSet):
    queryset = models.employee.objects.all()
    serializer_class = serializers.employeeSerializers #This will tell the viewset to use this serializerfor the conversion

    
    #Create - POST

    #Read - GET
    

    #Update - PUT

    #Delete - DELETE
