from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [

    path('', views.videos, name='videos'),
    path('students/', views.student_videos, name='student_videos'),
    path('parents/', views.parents_videos, name='parents_videos'),
    path('teachers/', views.teacher_videos, name='teachers_videos'),

]
