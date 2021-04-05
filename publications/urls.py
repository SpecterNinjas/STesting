from django.urls import path
from . import views

app_name = 'publications'

urlpatterns = [

    path('', views.publications, name='publications'),
    path('international/', views.international_publications, name='international_publications'),
    path('national/', views.national_publications, name='national_publications'),

]
