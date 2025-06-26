from django.urls import path

from . import views
urlpatterns = [
    path('', views.adminpanel),
    path('chat/', views.adminchat),
]
