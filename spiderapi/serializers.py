#Serializer for converting complex objects into native Python datatypes and deserialize parsed data back into complex types

from rest_framework import serializers
from spiderapi.models import Owners,Farms,Fields,Crops

class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Owners
        fields=('id','firstLast','phone','email')

class FarmsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Farms 
        fields=('id','ownerId','farmName','farmLocation','farmSize',)

class FieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fields 
        fields=('id','ownerId','farmId','fieldName','fieldSize','fertilizerType','lastFertilized','wateredAmount','lastWatered')


class CropsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crops 
        fields=('id','ownerId','farmId','fieldId','cropType','datePlanted','amountPlanted')



        
  
    