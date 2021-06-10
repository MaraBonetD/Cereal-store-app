from django.contrib.auth.models import User
from django.db import models
from products.models import Product

class OrderStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True) # if one status is deleted from the tables, then the orders will still be valid with that field been null
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField()
    price = models.FloatField()
    shipping_address = models.CharField(max_length=255)

    def __str__(self):
        return "{} /n {} /n {} /n {} /n {} /n {}".format(self.customer, self.order_status, self.created_at,
                                                         self.is_paid, self.price, self.shipping_address)

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

