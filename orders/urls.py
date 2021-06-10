from django.urls import path
from . import views

urlpatterns = [
    # http://localhost.../cerealsApp
    path('', views.index, name="orders_index"),
]