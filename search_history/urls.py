from django.urls import path
from . import views

urlpatterns = [
    # http://localhost.../cerealsApp
    path('', views.index, name="search_history_index"),
]

