from django.urls import path
from . import views

urlpatterns = [
    # http://localhost.../cerealsApp
    path('', views.get_search, name="search_results"),
]