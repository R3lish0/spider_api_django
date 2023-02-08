#Design your URL route here

from django.urls import path, re_path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


#URLConf
urlpatterns=[
    re_path(r'^Owners/?$', views.OwnersAPI),
    re_path(r'^Owners/([0-9]+)/?$', views.OwnersAPI, name='Owners'),

    re_path(r'^Farms/?$', views.FarmsAPI),
    re_path(r'^Farms/([0-9]+)/?$', views.FarmsAPI, name='Farms'),

    re_path(r'^Fields/?$', views.FieldsAPI),
    re_path(r'^Fields/([0-9]+)/?$', views.FieldsAPI, name='Fields'),

    re_path(r'^Crops/?$', views.CropsAPI),
    re_path(r'^Crops/([0-9]+)/?$', views.CropsAPI, name='Crops'),

    re_path(r'^GetOwners/?$', views.OwnersAPI),
    re_path(r'^GetOwners/([0-9]+)/?$', views.OwnersAPI, name='Owners'),

    re_path(r'^GetFarms/?$', views.GetFarmsAPI),
    re_path(r'^GetFarms/([0-9]+)/?$', views.GetFarmsAPI, name='Farms'),
    re_path(r'^GetFarms/([0-9]+)/([0-9])+/?$', views.GetFarmsAPI, name='Farms'),

    re_path(r'^GetFields/?$', views.GetFieldsAPI),
    re_path(r'^GetFields/([0-9]+)/?$', views.GetFieldsAPI, name='Fields'),
    re_path(r'^GetFields/([0-9]+)/([0-9]+)/?$', views.GetFieldsAPI, name='Fields'),
    re_path(r'^GetFields/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.GetFieldsAPI, name='Fields'),

    re_path(r'^GetCrops/?$', views.GetCropsAPI),
    re_path(r'^GetCrops/([0-9]+)/?$', views.GetCropsAPI, name='Crops'),
    re_path(r'^GetCrops/([0-9]+)/([0-9]+)/?$', views.GetCropsAPI, name='Crops'),
    re_path(r'^GetCrops/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.GetCropsAPI, name='Crops'),
    re_path(r'^GetCrops/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.GetCropsAPI, name='Crops'),

    re_path(r'^GetInputs/?$', views.GetInputsAPI),
    re_path(r'^GetInputs/([0-9]+)/?$', views.GetInputsAPI, name='Inputs'),
    re_path(r'^GetInputs/([0-9]+)/([0-9]+)/?$', views.GetInputsAPI, name='Inputs'),
    re_path(r'^GetInputs/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.GetInputsAPI, name='Inputs'),
    re_path(r'^GetInputs/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.GetInputsAPI, name='Inputs'),

    re_path(r'^GetSeeds/?$', views.GetSeedsAPI),
    re_path(r'^GetSeeds/([0-9]+)/?$', views.GetSeedsAPI, name='Seeds'),
    re_path(r'^GetSeeds/([0-9]+)/([0-9]+)/?$', views.GetSeedsAPI, name='Seeds'),
    re_path(r'^GetSeeds/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.GetSeedsAPI, name='Seeds'),


    re_path(r'^GetTests/?$', views.GetTestsAPI),
    re_path(r'^GetTests/([0-9]+)/?$', views.GetTestsAPI, name='Tests'),
    re_path(r'^GetTests/([0-9]+)/([0-9]+)/?$', views.GetTestsAPI, name='Tests'),
    re_path(r'^GetTests/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.GetTestsAPI, name='Tests'),


    re_path(r'^GetHarvests/?$', views.GetHarvestsAPI),
    re_path(r'^GetHarvests/([0-9]+)/?$', views.GetHarvestsAPI, name='Harvests'),
    re_path(r'^GetHarvests/([0-9]+)/([0-9]+)/?$', views.GetHarvestsAPI, name='Harvests'),
    re_path(r'^GetHarvests/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.GetHarvestsAPI, name='Harvests'),
    re_path(r'^GetHarvests/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.GetHarvestsAPI, name='Harvests')



]