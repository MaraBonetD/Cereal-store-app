from django.urls import path
from . import views

urlpatterns = [
    # http://localhost.../cerealsApp
    path('', views.order_history, name="order_history"),
    path('<int:id>', views.get_order_by_id, name='order_details')
]