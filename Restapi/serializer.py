from rest_framework import serializers
from .models import hospital
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=hospital
        fields=('id', 'name', 'state', 'city','pincode','latitude','longitude',  'type', 'Ratings', 'noOfDoctors', 'noOfBeds', 
        'diseases', 'treatments', 'link', 'image')
