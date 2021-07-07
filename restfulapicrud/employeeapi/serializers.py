# In order to access the api the python code needs to be converted to json format.
#The serializers define how to convert the data python to json/xml.
from rest_framework import serializers
from .models import employee

#We need to inherit the parent class of serializers, unser this class we define conversion

class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'   # This will include all the table attributes.