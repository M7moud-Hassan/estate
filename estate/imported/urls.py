from django.urls import path
from .views import *
urlpatterns=[
    path('',imported,name='home.imported'),
    path('add',add_imported,name='add_imported'),
    path('edit/<int:id>',edit_imported,name='edit_imported'),
    path('delete/<int:id>',delete_clients,name='delete_clients'),

]