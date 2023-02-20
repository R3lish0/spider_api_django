#Design your URL route here

from django.urls import path, re_path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


#URLConf
urlpatterns=[
    re_path(r'^Fields/?$', views.FieldsAPI),
    re_path(r'^Fields/([0-9]+)/?$', views.FieldsAPI, name='Fields'),

    re_path(r'^Crops/?$', views.CropsAPI),
    re_path(r'^Crops/([0-9]+)/?$', views.CropsAPI, name='Crops'),

    re_path(r'^Owners/?$', views.OwnersAPI),
    re_path(r'^Owners/([0-9]+)/?$', views.OwnersAPI, name='Owners'),

    re_path(r'^Farms/?$', views.FarmsAPI),
    re_path(r'^Farms/([0-9]+)/?$', views.FarmsAPI, name='Farms'),
    re_path(r'^Farms/([0-9]+)/([0-9])+/?$', views.FarmsAPI, name='Farms'),

    re_path(r'^Fields/?$', views.FieldsAPI),
    re_path(r'^Fields/([0-9]+)/?$', views.FieldsAPI, name='Fields'),
    re_path(r'^Fields/([0-9]+)/([0-9]+)/?$', views.FieldsAPI, name='Fields'),
    re_path(r'^Fields/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.FieldsAPI, name='Fields'),

    re_path(r'^Crops/?$', views.CropsAPI),
    re_path(r'^Crops/([0-9]+)/?$', views.CropsAPI, name='Crops'),
    re_path(r'^Crops/([0-9]+)/([0-9]+)/?$', views.CropsAPI, name='Crops'),
    re_path(r'^Crops/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.CropsAPI, name='Crops'),
    re_path(r'^Crops/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.CropsAPI, name='Crops'),

    re_path(r'^Inputs/?$', views.InputsAPI),
    re_path(r'^Inputs/([0-9]+)/?$', views.InputsAPI, name='Inputs'),
    re_path(r'^Inputs/([0-9]+)/([0-9]+)/?$', views.InputsAPI, name='Inputs'),
    re_path(r'^Inputs/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.InputsAPI, name='Inputs'),
    re_path(r'^Inputs/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.InputsAPI, name='Inputs'),

    re_path(r'^Seeds/?$', views.SeedsAPI),
    re_path(r'^Seeds/([0-9]+)/?$', views.SeedsAPI, name='Seeds'),
    re_path(r'^Seeds/([0-9]+)/([0-9]+)/?$', views.SeedsAPI, name='Seeds'),
    re_path(r'^Seeds/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.SeedsAPI, name='Seeds'),


    re_path(r'^Tests/?$', views.TestsAPI),
    re_path(r'^Tests/([0-9]+)/?$', views.TestsAPI, name='Tests'),
    re_path(r'^Tests/([0-9]+)/([0-9]+)/?$', views.TestsAPI, name='Tests'),
    re_path(r'^Tests/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.TestsAPI, name='Tests'),


    re_path(r'^Harvests/?$', views.HarvestsAPI),
    re_path(r'^Harvests/([0-9]+)/?$', views.HarvestsAPI, name='Harvests'),
    re_path(r'^Harvests/([0-9]+)/([0-9]+)/?$', views.HarvestsAPI, name='Harvests'),
    re_path(r'^Harvests/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.HarvestsAPI, name='Harvests'),
    re_path(r'^Harvests/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/?$', views.HarvestsAPI, name='Harvests')



]