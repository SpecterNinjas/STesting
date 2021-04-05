from django.urls import path
from . import views

app_name = 'researches'

urlpatterns = [

    path('', views.researches, name='researches'),
    path('international', views.inter_researches, name='inter_researches'),
    path('national', views.national_researches, name='national_researches'),

]
