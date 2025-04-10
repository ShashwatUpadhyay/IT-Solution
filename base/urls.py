from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('career/', views.career, name='career'),
    path('team/', views.team, name='team'),
]