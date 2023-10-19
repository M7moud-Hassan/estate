from django.contrib import admin
from django.urls import path,include
from  .views import *

urlpatterns = [
    path('',home,name="home"),
    path('projects/',projects,name="home.projects"),
    path('log_out/',log_out,name="log_out"),
]
