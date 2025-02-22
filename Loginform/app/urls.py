from django.urls import path
from app import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.user_login,name='login'),
    path('success/',views.success),

]