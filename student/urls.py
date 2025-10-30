from django.urls import path, include
from django.contrib.auth.decorators import login_required
from student import admin, views

urlpatterns = [
    path('/', views.student),
     
]