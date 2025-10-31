from django.urls import path
from web import views


urlpatterns = [
    path('', views.web),
    path('about/', views.about),
    path('career/', views.career),
    path('contact/', views.contact),
    path('academic/', views.academic),
    path('admission/', views.admission),
]