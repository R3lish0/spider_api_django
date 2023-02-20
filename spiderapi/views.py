#View which takes a request and returns a response

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#from django.http import HttpResponse

from spiderapi.models import Fields,Farms,Owners,Crops,Tests,Harvests,Seeds,Inputs
from spiderapi.serializers import FieldsSerializer,FarmsSerializer, OwnersSerializer, CropsSerializer, SeedsSerializer, HarvestsSerializer, TestsSerializer, InputsSerializer


# Create your views here.
#Request handler which takes requests and sends the response

@csrf_exempt
def OwnersAPI (request, ownId=0):
    if (request.method=='GET' and int(id) > 0):
        owners=Owners.objects.filter(id=ownId)
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
            owners=Owners.objects.get(id=owners_data['id'])
            owners_serializer=OwnersSerializer(Owners,data=owners_data)
            if owners_serializer.is_valid():
                owners_serializer.save()
                return JsonResponse("Record Updated Successfully",safe=False)
            return JsonResponse("There is some error updating the record", safe=False)
    elif request.method=='DELETE':
        owners=Owners.objects.get(id=ownId)
        owners.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def FarmsAPI (request, frmId=0, ownId=0):
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
    elif request.method=='POST':
        farms_data=JSONParser().parse(request)
        farms_serializer=FarmsSerializer(data=farms_data)
        if farms_serializer.is_valid():
            farms_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        farms_data=JSONParser().parse(request)
        farms=Farms.objects.get(id=farms_data['id'])
        farms_serializer=FarmsSerializer(farms,data=farms_data)
        if farms_serializer.is_valid():
            farms_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif (request.method=='DELETE' and int(frmId) > 0 and int(ownId) == 0):
        farms=Farms.objects.get(id=frmId)
        farms.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(frmId) == 0 and int(ownId) > 0):
        farms=Farms.objects.get(ownerId=ownId)
        farms.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def FieldsAPI (request, fldId = 0, frmId=0, ownId=0):
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
    elif request.method=='POST':
        fields_data=JSONParser().parse(request)
        fields_serializer=FieldsSerializer(data=fields_data)
        if fields_serializer.is_valid():
            fields_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        fields_data=JSONParser().parse(request)
        fields=Fields.objects.get(id=fields_data['id'])
        fields_serializer=FieldsSerializer(fields,data=fields_data)
        if fields_serializer.is_valid():
            fields_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif (request.method=='DELETE' and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        fields=Fields.objects.get(id=fldId)
        fields.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        fields=Fields.objects.get(farmId=frmId)
        fields.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        fields=Fields.objects.get(ownerId=ownId)
        fields.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def CropsAPI (request, crpId=0, fldId=0, frmId=0, ownId=0):
    if (request.method=='GET' and int(crpId) > 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
        crops=Crops.objects.filter(id=crpId)
        crops_serializer=CropsSerializer(crops, many=True)
        return JsonResponse(crops_serializer.data,safe=False)
    elif (request.method=='GET' and int(crpId) == 0 and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
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
    elif request.method=='POST':
        crops_data=JSONParser().parse(request)
        crops_serializer=CropsSerializer(data=crops_data)
        if crops_serializer.is_valid():
            crops_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        crops_data=JSONParser().parse(request)
        crops=Crops.objects.get(id=crops_data['id'])
        crops_serializer=CropsSerializer(crops,data=crops_data)
        if crops_serializer.is_valid():
            crops_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif (request.method=='DELETE' and int(crpId) > 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
        crops=Crops.objects.get(id=crpId)
        crops.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(crpId) == 0 and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        crops=Crops.objects.get(fieldId=fldId)
        crops.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(crpId) == 0 and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        crops=Crops.objects.get(farmId=frmId)
        crops.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(crpId) == 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        crops=Crops.objects.get(ownerId=ownId)
        crops.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def HarvestsAPI (request, hrvstId=0, crpId=0, fldId=0, frmId=0, ownId=0):
    if (request.method=='GET' and int(hrvstId) > 0 and int(crpId) == 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
        harvests=Harvests.objects.filter(id=hrvstId)
        harvests_serializer=HarvestsSerializer(harvests, many=True)
    elif (request.method=='GET' and int(hrvstId) == 0 and int(crpId) > 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
        harvests=Harvests.objects.filter(cropId=crpId)
        harvests_serializer=HarvestsSerializer(harvests, many=True)
        return JsonResponse(harvests_serializer.data,safe=False)
    elif (request.method=='GET' and int(hrvstId) == 0 and int(crpId) == 0 and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        harvests=Harvests.objects.filter(fieldId=fldId)
        harvests_serializer=HarvestsSerializer(harvests, many=True)
        return JsonResponse(harvests_serializer.data,safe=False)
    elif (request.method=='GET' and int(hrvstId) == 0 and int(crpId) == 0 and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        harvests=Harvests.objects.filter(farmId=frmId)
        harvests_serializer=HarvestsSerializer(harvests, many=True)
        return JsonResponse(harvests_serializer.data,safe=False)
    elif (request.method=='GET' and int(hrvstId) == 0 and int(crpId) == 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        harvests=Harvests.objects.filter(owner=ownId)
        harvests_serializer=HarvestsSerializer(harvests, many=True)
        return JsonResponse(harvests_serializer.data,safe=False)
    elif (request.method=='GET'):
        harvests=Harvests.objects.all()
        harvests_serializer=HarvestsSerializer(harvests, many=True)
        return JsonResponse(harvests_serializer.data,safe=False)
    elif request.method=='POST':
        harvests_data=JSONParser().parse(request)
        harvests_serializer=HarvestsSerializer(data=harvests_data)
        if harvests_serializer.is_valid():
            harvests_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        harvests_data=JSONParser().parse(request)
        harvests=Harvests.objects.get(id=harvests_data['id'])
        harvests_serializer=HarvestsSerializer(harvests,data=harvests_data)
        if harvests_serializer.is_valid():
            harvests_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif (request.method=='DELETE' and int(hrvstId) > 0 and int(crpId) == 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
        harvests=Harvests.objects.get(id=hrvstId)
        harvests.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(hrvstId) == 0 and int(crpId) > 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
        harvests=Harvests.objects.get(cropId=crpId)
        harvests.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(hrvstId) == 0 and int(crpId) == 0 and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        harvests=Harvests.objects.get(fieldId=fldId)
        harvests.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(hrvstId) == 0 and int(crpId) == 0 and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        harvests=Harvests.objects.get(farmId=frmId)
        harvests.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(hrvstId) == 0 and int(crpId) == 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        harvests=Harvests.objects.get(ownerId=ownId)
        harvests.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def TestsAPI (request, tstId = 0, frmId=0, ownId=0):
    if (request.method=='GET' and int(tstId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        tests=Tests.objects.filter(id=tstId)
        tests_serializer=TestsSerializer(tests, many=True)
        return JsonResponse(tests_serializer.data,safe=False)
    elif (request.method=='GET' and int(tstId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        tests=Tests.objects.filter(Farmid=frmId)
        tests_serializer=TestsSerializer(tests, many=True)
        return JsonResponse(tests_serializer.data,safe=False)
    elif (request.method=='GET' and int(tstId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        tests=Tests.objects.filter(ownerId=ownId)
        tests_serializer=TestsSerializer(tests, many=True)
        return JsonResponse(tests_serializer.data,safe=False)
    elif (request.method=='GET'):
        tests = Farms.objects.all()
        tests_serializer=TestsSerializer(tests, many=True)
        return JsonResponse(tests_serializer.data,safe=False)
    elif (request.method=='GET'):
        tests=Tests.objects.all()
        tests_serializer=TestsSerializer(tests, many=True)
        return JsonResponse(tests_serializer.data,safe=False)
    elif request.method=='POST':
        tests_data=JSONParser().parse(request)
        tests_serializer=TestsSerializer(data=tests_data)
        if tests_serializer.is_valid():
            tests_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        tests_data=JSONParser().parse(request)
        tests=Tests.objects.get(id=tests_data['id'])
        tests_serializer=TestsSerializer(tests,data=tests_data)
        if tests_serializer.is_valid():
            tests_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif (request.method=='DELETE' and int(tstId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        tests=Tests.objects.get(id=tstId)
        tests.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(tstId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        tests=Tests.objects.get(farmId=frmId)
        tests.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(tstId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        tests=Tests.objects.get(ownerId=ownId)
        tests.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def SeedsAPI (request, sdsId = 0, frmId=0, ownId=0):
    if (request.method=='GET' and int(sdsId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        seeds=Seeds.objects.filter(id=sdsId)
        seeds_serializer=SeedsSerializer(seeds, many=True)
        return JsonResponse(seeds_serializer.data,safe=False)
    elif (request.method=='GET' and int(sdsId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        seeds=Seeds.objects.filter(farmId=frmId)
        seeds_serializer=SeedsSerializer(seeds, many=True)
        return JsonResponse(seeds_serializer.data,safe=False)
    elif (request.method=='GET' and int(sdsId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        seeds=Seeds.objects.filter(ownerId=ownId)
        seeds_serializer=SeedsSerializer(seeds, many=True)
        return JsonResponse(seeds_serializer.data,safe=False)
    elif (request.method=='GET'):
        seeds = Seeds.objects.all()
        seeds_serializer=SeedsSerializer(seeds,many=True)
        return JsonResponse(seeds_serializer.data,safe=False)
    elif (request.method=='GET'):
        seeds=seeds.objects.all()
        seeds_serializer=SeedsSerializer(seeds, many=True)
        return JsonResponse(seeds_serializer.data,safe=False)
    elif request.method=='POST':
        seeds_data=JSONParser().parse(request)
        seeds_serializer=SeedsSerializer(data=seeds_data)
        if seeds_serializer.is_valid():
            seeds_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        seeds_data=JSONParser().parse(request)
        seeds=Seeds.objects.get(id=seeds_data['id'])
        seeds_serializer=SeedsSerializer(seeds,data=seeds_data)
        if seeds_serializer.is_valid():
            seeds_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif (request.method=='DELETE' and int(sdsId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        tests=Tests.objects.get(id=sdsId)
        tests.delete()
    elif (request.method=='DELETE' and int(sdsId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        tests=Tests.objects.get(farmId=frmId)
        tests.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(sdsId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        tests=Tests.objects.get(ownerId=ownId)
        tests.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def InputsAPI (request, inpId=0, fldId=0, frmId=0, ownId=0):
    if (request.method=='GET' and int(inpId) > 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
        inputs=Inputs.objects.filter(id=inpId)
        inputs_serializer=InputsSerializer(inputs, many=True)
        return JsonResponse(inputs_serializer.data,safe=False)
    if (request.method=='GET' and int(inpId) == 0 and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
        inputs=Inputs.objects.filter(fieldId=fldId)
        inputs_serializer=InputsSerializer(inputs, many=True)
        return JsonResponse(inputs_serializer.data,safe=False)
    elif (request.method=='GET' and int(inpId) == 0 and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        inputs=Inputs.objects.filter(farmId=frmId)
        inputs_serializer=InputsSerializer(inputs, many=True)
        return JsonResponse(inputs_serializer.data,safe=False)
    elif (request.method=='GET'and int(inpId) == 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        inputs=Inputs.objects.filter(ownerId=ownId)
        inputs_serializer=InputsSerializer(inputs, many=True)
        return JsonResponse(inputs_serializer.data,safe=False)
    elif (request.method=='GET'):
        inputs = Inputs.objects.all()
        inputs_serializer=InputsSerializer(inputs,many=True)
        return JsonResponse(inputs_serializer.data,safe=False)
    elif request.method=='POST':
        inputs_data=JSONParser().parse(request)
        inputs_serializer=InputsSerializer(data=inputs_data)
        if inputs_serializer.is_valid():
            inputs_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        inputs_data=JSONParser().parse(request)
        inputs=Inputs.objects.get(id=inputs_data['id'])
        inputs_serializer=InputsSerializer(inputs,data=inputs_data)
        if inputs_serializer.is_valid():
            inputs_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif (request.method=='DELETE' and int(inpId) > 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
        inputs=Inputs.objects.get(id=inpId)
        inputs.delete()
    elif (request.method=='DELETE' and int(inpId) == 0 and int(fldId) > 0 and int(frmId) > 0 and int(ownId) == 0):
        inputs=Inputs.objects.get(fieldId=fldId)
        inputs.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(inpId) == 0 and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
        inputs=Inputs.objects.get(farmId=frmId)
        inputs.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)
    elif (request.method=='DELETE' and int(inpId) == 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
        inputs=Inputs.objects.get(ownerId=ownId)
        inputs.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)


#@csrf_exempt
#def GetFarmsAPI (request, frmId=0, ownId=0):
#    if (request.method=='GET' and int(frmId) > 0 and int(ownId) == 0):
#        farms=Farms.objects.filter(id=frmId)
#        farms_serializer=FarmsSerializer(farms, many=True)
#       return JsonResponse(farms_serializer.data,safe=False)
#    elif (request.method=='GET' and int(frmId) == 0 and int(ownId) > 0):
#        farms=Farms.objects.filter(ownerId=ownId)
#        farms_serializer=FarmsSerializer(farms, many=True)
#        return JsonResponse(farms_serializer.data,safe=False)
#    elif (request.method=='GET'):
#        farms = Farms.objects.all()
#        farms_serializer=FarmsSerializer(farms,many=True)
#        return JsonResponse(farms_serializer.data,safe=False)

#@csrf_exempt
#def GetOwnersAPI (request, ownId=0):
#   if (request.method=='GET' and int(ownId) == 0):
#        owners=Owners.objects.filter(id=ownId)
#        owners_serializer=OwnersSerializer(owners, many=True)
#        return JsonResponse(owners_serializer.data,safe=False)
#    elif (request.method=='GET'):
#        owners = Owners.objects.all()
#        owners_serializer=OwnersSerializer(owners,many=True)
#        return JsonResponse(owners_serializer.data,safe=False)


#@csrf_exempt
#def GetFieldsAPI (request, fldId = 0, frmId=0, ownId=0):
#    if (request.method=='GET' and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
#        fields=Fields.objects.filter(id=fldId)
#        fields_serializer=FieldsSerializer(fields, many=True)
#        return JsonResponse(fields_serializer.data,safe=False)
#    elif (request.method=='GET' and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
#        fields=Fields.objects.filter(farmId=frmId)
#        fields_serializer=FieldsSerializer(fields, many=True)
#        return JsonResponse(fields_serializer.data,safe=False)
#    elif (request.method=='GET' and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
#        fields=Fields.objects.filter(ownerId=ownId)
#        fields_serializer=FieldsSerializer(fields, many=True)
#        return JsonResponse(fields_serializer.data,safe=False)
#    elif (request.method=='GET'):
#        fields = Fields.objects.all()
#        fields_serializer=FieldsSerializer(fields,many=True)
#        return JsonResponse(fields_serializer.data,safe=False)

#@csrf_exempt
#def GetCropsAPI (request, crpId=0, fldId=0, frmId=0, ownId=0):
#    if (request.method=='GET' and int(crpId) > 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
#        crops=Crops.objects.filter(id=crpId)
#        crops_serializer=CropsSerializer(crops, many=True)
#        return JsonResponse(crops_serializer.data,safe=False)
#    if (request.method=='GET' and int(crpId) == 0 and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
#        crops=Crops.objects.filter(fieldId=fldId)
#        crops_serializer=CropsSerializer(crops, many=True)
#        return JsonResponse(crops_serializer.data,safe=False)
#    elif (request.method=='GET' and int(crpId) == 0 and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
#        crops=Crops.objects.filter(farmId=frmId)
#        crops_serializer=CropsSerializer(crops, many=True)
#        return JsonResponse(crops_serializer.data,safe=False)
#    elif (request.method=='GET'and int(crpId) == 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
#       crops=Crops.objects.filter(ownerId=ownId)
#        crops_serializer=CropsSerializer(crops, many=True)
#        return JsonResponse(crops_serializer.data,safe=False)
#    elif (request.method=='GET'):
#        crops = Crops.objects.all()
#        crops_serializer=CropsSerializer(crops,many=True)
#        return JsonResponse(crops_serializer.data,safe=False)
    


#@csrf_exempt
#def GetSeedsAPI (request, sdsId = 0, frmId=0, ownId=0):
#    if (request.method=='GET' and int(sdsId) > 0 and int(frmId) == 0 and int(ownId) == 0):
#        seeds=Seeds.objects.filter(id=sdsId)
#        seeds_serializer=SeedsSerializer(seeds, many=True)
#        return JsonResponse(seeds_serializer.data,safe=False)
#    elif (request.method=='GET' and int(sdsId) == 0 and int(frmId) > 0 and int(ownId) == 0):
#        seeds=Seeds.objects.filter(farmId=frmId)
#        seeds_serializer=SeedsSerializer(seeds, many=True)
#        return JsonResponse(seeds_serializer.data,safe=False)
#    elif (request.method=='GET' and int(sdsId) == 0 and int(frmId) == 0 and int(ownId) > 0):
#        seeds=Seeds.objects.filter(ownerId=ownId)
#        seeds_serializer=SeedsSerializer(seeds, many=True)
#        return JsonResponse(seeds_serializer.data,safe=False)
#    elif (request.method=='GET'):
#        seeds = Seeds.objects.all()
#        seeds_serializer=SeedsSerializer(seeds,many=True)
#        return JsonResponse(seeds_serializer.data,safe=False)

#@csrf_exempt
#def GetInputsAPI (request, inpId=0, fldId=0, frmId=0, ownId=0):
#    if (request.method=='GET' and int(inpId) > 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) == 0):
#        inputs=Inputs.objects.filter(id=inpId)
#        inputs_serializer=InputsSerializer(inputs, many=True)
#        return JsonResponse(inputs_serializer.data,safe=False)
#    if (request.method=='GET' and int(inpId) == 0 and int(fldId) > 0 and int(frmId) == 0 and int(ownId) == 0):
#        inputs=Inputs.objects.filter(fieldId=fldId)
#        inputs_serializer=InputsSerializer(inputs, many=True)
#        return JsonResponse(inputs_serializer.data,safe=False)
#    elif (request.method=='GET' and int(inpId) == 0 and int(fldId) == 0 and int(frmId) > 0 and int(ownId) == 0):
#        inputs=Inputs.objects.filter(farmId=frmId)
#        inputs_serializer=InputsSerializer(inputs, many=True)
#        return JsonResponse(inputs_serializer.data,safe=False)
#    elif (request.method=='GET'and int(inpId) == 0 and int(fldId) == 0 and int(frmId) == 0 and int(ownId) > 0):
#        inputs=Inputs.objects.filter(ownerId=ownId)
#        inputs_serializer=InputsSerializer(inputs, many=True)
#        return JsonResponse(inputs_serializer.data,safe=False)
#    elif (request.method=='GET'):
#        inputs = Inputs.objects.all()
#        inputs_serializer=InputsSerializer(inputs,many=True)
#        return JsonResponse(inputs_serializer.data,safe=False)