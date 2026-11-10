from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/add/', views.create_contact, name='create_contact'),
    path('contacts/<int:pk>/edit/', views.update_contact, name='update_contact'),
    path('contacts/delete/', views.delete_contact, name='delete_contact'),
]
