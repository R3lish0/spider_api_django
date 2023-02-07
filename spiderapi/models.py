#A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table

from math import fabs
from django.db import models

# Create your models here.

class Owners(models.Model):
    id = models.AutoField(primary_key=True)
    firstLast = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    
    def __str__(self):
        return self.id

class Farms(models.Model):
    id = models.AutoField(primary_key=True)
    ownerId = models.IntegerField(blank=False)
    farmName = models.CharField(max_length=500)
    farmLocation = models.CharField(max_length=500)
    farmSize = models.IntegerField(blank=False)
    

    def __str__(self):
        return self.id


class Fields(models.Model):
    id = models.AutoField(primary_key=True)
    ownerId = models.IntegerField(blank=False)
    farmId = models.IntegerField(blank=False)
    fieldName = models.CharField(max_length=500)
    fieldSize = models.IntegerField(blank=False)
    fertilizerType = models.CharField(max_length=500)
    lastFertilized = models.DateField()
    wateredAmount = models.IntegerField()
    lastWatered = models.DateField()

    def __str__(self):
        return self.id


class Crops(models.Model):
    id = models.AutoField(primary_key=True)
    ownerId = models.IntegerField(blank=False)
    farmId = models.IntegerField(blank=False)
    fieldId = models.IntegerField(blank=False)
    cropType = models.CharField(max_length=500)
    datePlanted = models.DateField()
    amountPlanted = models.IntegerField(blank=False)
    
    def __str__(self):
        return self.id


class Inputs(models.Model):
    id = models.AutoField(primary_key=True)
    ownerId = models.IntegerField(blank=False)
    farmId = models.IntegerField(blank=False)
    fieldId = models.IntegerField(blank=False)
    input = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    applicationRate = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    purpose = models.CharField(max_length=500)
    applicator = models.CharField(max_length=100)
    windSpeed = models.CharField(max_length=50)
    windDirection = models.CharField(max_length=30)
    equipmentUsed = models.CharField(max_length=200)
    equipmentCleanup = models.CharField(max_length=150)
    isApproved = models.BooleanField()
    msds = models.CharField(max_length=100)
    other = models.CharField(max_length=200)

    
    def __str__(self):
        return self.id


class Harvests(models.Model):
    id = models.AutoField(primary_key=True)
    ownerId = models.IntegerField(blank=False)
    farmId = models.IntegerField(blank=False)
    fieldId = models.IntegerField(blank=False)
    cropId = models.IntegerField(blank=False)
    harvestMethod = models.CharField(max_length=200)
    harvestCrew = models.CharField(max_length=200)
    equipmentCleanup = models.CharField(max_length=200)
    harvestYield = models.CharField(max_length=200)
    produceCleanup = models.CharField(max_length=200)
    storage = models.CharField(max_length=300)
    transportation = models.CharField(max_length=300)
    soldAmount = models.CharField(max_length=200)
    leftOverAmount = models.CharField(max_length=200)
    salesReceipt = models.CharField(max_length=200)


    
    def __str__(self):
        return self.id


class Seeds(models.Model):
    id = models.AutoField(primary_key=True)
    ownerId = models.IntegerField(blank=False)
    farmId = models.IntegerField(blank=False)
    seedName = models.CharField(max_length=200)
    variety = models.CharField(max_length=200)
    sourceOne = models.CharField(max_length=200)
    sourceTwo = models.CharField(max_length=200)
    sourceThree = models.CharField(max_length=200)
    org = models.CharField(max_length=200)
    treatment = models.CharField(max_length=200)
    plantingDate = models.DateField()
    location = models.CharField(max_length=200)
    plantingCrew = models.CharField(max_length=200)


    
    def __str__(self):
        return self.id


class Tests(models.Model):
    id = models.AutoField(primary_key=True)
    ownerId = models.IntegerField(blank=False)
    farmId = models.IntegerField(blank=False)
    testingVariable = models.CharField(max_length=200)
    numSamples = models.IntegerField()
    collectionDate = models.DateField()
    location = models.CharField(max_length=200)
    testingCompany = models.CharField(max_length=200)
    resultDate = models.DateField()
    resultsSaved = models.CharField(max_length=200)


    
    def __str__(self):
        return self.id
