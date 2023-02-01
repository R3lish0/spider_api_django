#View which takes a request and returns a response

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#from django.http import HttpResponse

from spiderapi.models import Fields,Farms,Owners,Crops
from spiderapi.serializers import FieldsSerializer,FarmsSerializer, OwnersSerializer, CropsSerializer


# Create your views here.
#Request handler which takes requests and sends the response

@csrf_exempt
def OwnersAPI (request, id=0):
    if (request.method=='GET' and int(id) > 0):
        owners=Owners.objects.filter(OwnersId=id)
        owners_serializer=OwnersSerializer(owners, many=True)
        return JsonResponse(owners_serializer.data,safe=False)
    elif request.method=='GET':   
        owners = Owners.objects.all()
        owners_serializer=OwnersSerializer(owners,many=True)
        return JsonResponse(owners_serializer.data,safe=False)
    elif request.method=='POST':
            owners_data=JSONParser().parse(request)
            owners_serializer=OwnersSerializer(data=owners_data)
            if owners_serializer.is_valid():
                owners_serializer.save()
                return JsonResponse("Record Inserted Successfully",safe=False)
            return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
            owners_data=JSONParser().parse(request)
            owners=Owners.objects.get(ownersId=owners_data['id'])
            owners_serializer=OwnersSerializer(Owners,data=owners_data)
            if owners_serializer.is_valid():
                owners_serializer.save()
                return JsonResponse("Record Updated Successfully",safe=False)
            return JsonResponse("There is some error updating the record", safe=False)
    elif request.method=='DELETE':
        owners=Owners.objects.get(OwnersId=id)
        owners.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def FarmsAPI (request, id=0):
    if (request.method=='GET' and int(id) > 0):
        farms=Farms.objects.filter(FarmsId=id)
        farms_serializer=FarmsSerializer(farms, many=True)
        return JsonResponse(farms_serializer.data,safe=False)
    elif request.method=='GET':
        farms =  Farms.objects.all()
        farms_serializer=FarmsSerializer(farms,many=True)
        return JsonResponse(farms_serializer.data,safe=False)
    elif request.method=='POST':
        farms_data=JSONParser().parse(request)
        farms_serializer=FarmsSerializer(data=farms_data)
        if farms_serializer.is_valid():
            farms_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        farms_data=JSONParser().parse(request)
        farms=Farms.objects.get(FarmsId=farms_data['id'])
        farms_serializer=FarmsSerializer(farms,data=farms_data)
        if farms_serializer.is_valid():
            farms_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif request.method=='DELETE':
        farms=Farms.objects.get(FarmsId=id)
        farms.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def FieldsAPI (request, id=0):
    if (request.method=='GET' and int(id) > 0):
        fields=Fields.objects.filter(FieldsId=id)
        fields_serializer=FieldsSerializer(fields, many=True)
        return JsonResponse(fields_serializer.data,safe=False)
    elif request.method=='GET':
        fields = Fields.objects.all()
        fields_serializer=FieldsSerializer(fields,many=True)
        return JsonResponse(fields_serializer.data,safe=False)
    elif request.method=='POST':
        fields_data=JSONParser().parse(request)
        fields_serializer=FieldsSerializer(data=fields_data)
        if fields_serializer.is_valid():
            fields_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        fields_data=JSONParser().parse(request)
        fields=Fields.objects.get(FieldsId=fields_data['id'])
        fields_serializer=FieldsSerializer(fields,data=fields_data)
        if fields_serializer.is_valid():
            fields_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif request.method=='DELETE':
        fields=Fields.objects.get(FieldsId=id)
        fields.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def CropsAPI (request, id=0):
    if (request.method=='GET' and int(id) > 0):
        crops=Crops.objects.filter(CropsId=id)
        crops_serializer=CropsSerializer(crops, many=True)
        return JsonResponse(crops_serializer.data,safe=False)
    elif request.method=='GET':
        crops =  Crops.objects.all()
        crops_serializer=CropsSerializer(crops,many=True)
        return JsonResponse(crops_serializer.data,safe=False)
    elif request.method=='POST':
        crops_data=JSONParser().parse(request)
        crops_serializer=CropsSerializer(data=crops_data)
        if crops_serializer.is_valid():
            crops_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        crops_data=JSONParser().parse(request)
        crops=Crops.objects.get(CropsId=crops_data['id'])
        crops_serializer=CropsSerializer(crops,data=crops_data)
        if crops_serializer.is_valid():
            crops_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif request.method=='DELETE':
        crops=Crops.objects.get(ProductId=id)
        crops.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

csrf_exempt
def GetFarmsAPI (request, frmId=0, ownId=0):
    if (request.method=='GET' and int(frmId) > 0 and int(ownId) == 0):
        farms=Farms.objects.filter(id=frmId)
        farms_serializer=FarmsSerializer(farms, many=True)
        return JsonResponse(farms_serializer.data,safe=False)
    elif (request.method=='GET' and int(frmId) == 0 and int(ownId) > 0):
        farms=Farms.objects.filter(ownerId=ownId)
        farms_serializer=FarmsSerializer(farms, many=True)
        return JsonResponse(farms_serializer.data,safe=False)
    elif (request.method=='GET'):
        farms = Farms.objects.all()
        farms_serializer=FarmsSerializer(farms,many=True)
        return JsonResponse(farms_serializer.data,safe=False)

csrf_exempt
def GetFieldsAPI (request, fldId = 0, frmId=0, ownId=0):
    if (request.method=='GET' and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        fields=Fields.objects.filter(id=fldId)
        fields_serializer=FieldsSerializer(fields, many=True)
        return JsonResponse(fields_serializer.data,safe=False)
    elif (request.method=='GET' and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        fields=Fields.objects.filter(farmId=frmId)
        fields_serializer=FieldsSerializer(fields, many=True)
        return JsonResponse(fields_serializer.data,safe=False)
    elif (request.method=='GET' and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        fields=Fields.objects.filter(ownerId=ownId)
        fields_serializer=FieldsSerializer(fields, many=True)
        return JsonResponse(fields_serializer.data,safe=False)
    elif (request.method=='GET'):
        fields = Fields.objects.all()
        fields_serializer=FieldsSerializer(fields,many=True)
        return JsonResponse(fields_serializer.data,safe=False)

csrf_exempt
def GetCropsAPI (request, crpId=0, fldId=0, frmId=0, ownId=0):
    if (request.method=='GET' and int(crpId) > 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
        crops=Crops.objects.filter(id=crpId)
        crops_serializer=CropsSerializer(crops, many=True)
        return JsonResponse(crops_serializer.data,safe=False)
    if (request.method=='GET' and int(crpId) == 0 and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        crops=Crops.objects.filter(fieldId=fldId)
        crops_serializer=CropsSerializer(crops, many=True)
        return JsonResponse(crops_serializer.data,safe=False)
    elif (request.method=='GET' and int(crpId) == 0 and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        crops=Crops.objects.filter(farmId=frmId)
        crops_serializer=CropsSerializer(crops, many=True)
        return JsonResponse(crops_serializer.data,safe=False)
    elif (request.method=='GET'and int(crpId) == 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        crops=Crops.objects.filter(ownerId=ownId)
        crops_serializer=CropsSerializer(crops, many=True)
        return JsonResponse(crops_serializer.data,safe=False)
    elif (request.method=='GET'):
        crops = Crops.objects.all()
        crops_serializer=CropsSerializer(crops,many=True)
        return JsonResponse(crops_serializer.data,safe=False)
    