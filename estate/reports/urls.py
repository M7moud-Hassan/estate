from django.urls import path
from .views import *
urlpatterns=[
    path('',reports,name='home.report'),
    # path('add-engineer/',add,name='add_engineer'),
    # path('edit-engineer/<int:pk>',edit,name='edit_engineer'),
    # path('delete-engineer/<int:pk>',delete,name='delete_engineer'),
    # path('details/<int:pk>',details,name='details_engineer')
]