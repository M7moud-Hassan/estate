
from django.contrib import admin
from django.urls import path,include

from .views import  *
urlpatterns = [
  path('add_project/',add_project,name="add_project"),
  path('edit_project/<int:id>/',edit_project,name="edit_project"),
  path('update_ahdaa/',update_ahdaa,name="update_ahdaa"),
  path('update_masrouf/',update_masrouf,name='update_masrouf'),
  path('delete_project/<int:id>/',delete_project,name='delete_project'),
  path('form/',form,name='form'),
  path('add_duration/',add_duration,name="add_duration"),
  path('delete_duration/',delete_duration,name="delete_duration"),
  path('delete_masrouf/',delete_masrouf,name="delete_masrouf"),
  # path('add_duration/',edd_duration,name="add_duration"),
  path('add_imported/',add_imported,name="add_importeds")
]
