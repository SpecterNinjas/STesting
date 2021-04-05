from django.urls import path
from . import views


app_name = 'researches'

urlpatterns = [

    path('', views.researches, name='researches'),


]
