from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('savemsg/', views.savemsg, name='savemsg'),
    path('about/', views.about, name='about'),

# services=========================
    path('android-development/', views.ad, name='ad'),
    path('digital-marketing/', views.dm, name='dm'),
    path('graphic-design/', views.gd, name='gd'),
    path('grow-your-business/', views.gyb, name='gyb'),
    path('logo-designing/', views.ld, name='ld'),
    path('mobile-app-development/', views.mad, name='mad'),
    path('web-development/', views.wd, name='wd'),
    path('web-maintenance/', views.wm, name='wm'),
]