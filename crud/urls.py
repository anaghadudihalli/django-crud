from django.urls import path

from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.read, name='read'),
    path('create/', views.create, name='create'),
    path('<int:publications_id>/update/', views.update, name='update'),
    path('<int:publications_id>/delete/', views.delete, name='delete'),
    path('add/', views.add, name='add'),
    path('<int:publications_id>/edit/', views.edit, name='edit'),
    path('add_students/', views.add_students, name='add_students'),
    path('add_s/', views.add_s, name='add_s')
]