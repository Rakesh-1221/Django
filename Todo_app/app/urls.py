from django.urls import path
from app import views

urlpatterns = [
    path('', views.create, name='create'),  # This route points to the create view for adding students
    path('update/<int:id>/', views.edit, name='update'),  # Route for editing a student by ID
    path('delete/<int:id>/', views.delete, name='delete'),  # Route for deleting a student by ID
]