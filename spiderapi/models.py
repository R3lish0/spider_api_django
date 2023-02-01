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
    wateredAmount = models.IntegerField(blank=False)
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
