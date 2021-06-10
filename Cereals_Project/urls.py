"""Cereals_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkout/', include('checkout.urls')),
    path('details/', include('details.urls')),
    path('order_history/', include('order_history.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('profiles/', include('profiles.urls')),
    path('search/', include('search.urls')),
    path('search_history/', include('search_history.urls')),
    path('shopping_cart/', include('shopping_cart.urls')),
    path('users/', include('users.urls')),
]
