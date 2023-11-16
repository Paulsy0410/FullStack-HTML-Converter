
from django.urls import path,include
from .views import *

urlpatterns = [
   
     path('',convertor_view, name='convertor_view'),
]

