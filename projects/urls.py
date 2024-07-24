from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create, name='project_create'),
    path('<int:pk>/edit/', views.project_update, name='project_update'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('<int:project_pk>/tasks/create/', views.task_create, name='task_create'),
    path('<int:project_pk>/tasks/<int:task_pk>/edit/', views.task_detail, name='task_detail'),
    path('<int:project_pk>/tasks/<int:task_pk>/detail/', views.task_update, name='task_update'),
    path('<int:project_pk>/tasks/<int:task_pk>/delete/', views.task_delete, name='task_delete'),
]
