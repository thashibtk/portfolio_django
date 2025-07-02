from django.urls import include, path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('project/1/', views.project_details, name='project_details'),
    path('contact/', views.contact, name='contact'),
]
