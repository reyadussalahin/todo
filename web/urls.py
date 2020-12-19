from django.urls import path

from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<str:todo_id>/', views.detail, name='detail'),
    path('<str:todo_id>/update/', views.update, name='update'),
    path('<str:todo_id>/update_status/', views.update_status, name='update_status'),
    path('<str:todo_id>/delete/', views.delete, name='delete'),
]
