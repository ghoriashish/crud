from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    
    path("",views.homepage,name="homepage"),
    path("registeruser/",views.registeruser,name="registeruser"),
    path("showdata/",views.showdata,name="showdata"),
    path("success/",views.success,name="success"),
    path("edit/",views.edit,name="edit"),
    path("change/",views.change,name="change"),
    path("delete/",views.delete,name="delete"),
]
