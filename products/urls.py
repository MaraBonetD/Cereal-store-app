from django.urls import path
from . import views

urlpatterns = [
    # http://localhost.../cerealsApp
    path('', views.index, name="products_index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('create_new_product', views.create_new_product, name="create_new_product"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),
    path('update_product/<int:id>', views.update_product, name="update_product"),
    path('add_review/<int:id>' , views.add_review, name="add_review")
]
