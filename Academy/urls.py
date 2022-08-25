from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('student', views.StudentView, name='student'),
    path('course', views.CourseView, name='course'),
]
