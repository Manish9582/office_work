"""
URL configuration for wealth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('',views.deshboard),
    path('mutual-funds/',views.mutual_funds),
    path('user/',include('verify.urls')),
    path('fixed-deposits/',views.fixed_deposit),
    path('post-office/',views.post_office),
    path('insurance/',views.insurance),
    path('aifs/',views.aif),
    path('api-funds/',views.funds),
    path('stocks/',views.stocks),
    path('bonds/',views.bonds),
    path('market/',views.market),
    # path('user_page/',include('userinfo.urls')),
    # path('admin_page/',include('admininfo.urls')),
]
