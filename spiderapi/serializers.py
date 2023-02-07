#Serializer for converting complex objects into native Python datatypes and deserialize parsed data back into complex types

from rest_framework import serializers
from spiderapi.models import Owners,Farms,Fields,Crops,Inputs,Harvests,Seeds,Tests

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


class InputsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inputs 
        fields=('id','ownerId','farmID','fieldId','input','manufacturer','date','time','purpose','applicator','windSpeed','windDirection','equipmentUsed','isApproved','msds','other')


class HarvestsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Harvests 
        fields=('id','ownerId','farmId','fieldId','cropId','harvestMethod','harvestCrew','equipmentCleanup','harvestYield','produceCleanup','storage','transportation','soldAmount','leftOverAmount','saleReceipt')


class SeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seeds 
        fields=('id','ownerId','farmId','seedName','variety','sourceOne','sourceTwo','sourceThree','org','treatment','plantingDate','location','plantingCrew')


class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tests
        fields=('id','ownerId','farmId','testingVariable','numSamples','collectionDate','location','testingCompany','resultDate','resultsSaved')

        
  
    