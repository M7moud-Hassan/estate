from django.urls import path
from .views import *
urlpatterns=[
    path('',reports,name='home.report'),
     path('mos_report/<int:pk>/',mos_report,name="mos_report"),
     path('durations_report/<int:pk>/',durations_report,name="durations_report"),
     path('masrouf_report/<int:pk>/',masrouf_report,name="masrouf_report"),
     path('details_report/<int:pk>/',details_report,name="details_report"),
     path('finance_report/<int:pk>/',finance_report,name="finance_report"),
     path('ahdaa_report/<int:pk>/',ahdaa_report,name="ahdaa_report"),
     
    # path('add-engineer/',add,name='add_engineer'),
    # path('edit-engineer/<int:pk>',edit,name='edit_engineer'),
    # path('delete-engineer/<int:pk>',delete,name='delete_engineer'),
    # path('details/<int:pk>',details,name='details_engineer')
]