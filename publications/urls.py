from django.urls import path
from . import views


app_name = 'publications'

urlpatterns = [

    path('', views.publications, name='publications'),


]