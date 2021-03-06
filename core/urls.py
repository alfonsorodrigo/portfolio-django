from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(),  name="home"),
    path('about-me/', views.About.as_view(), name="about"),
    path('contact/', views.Contact.as_view(), name="contact"),
]
