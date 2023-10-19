from django.urls import path, include
from .views import *
urlpatterns = [
    path('login_view/',login_view,name='login_view')
]