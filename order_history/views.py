from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from order_history.models import Order, OrderDetails
from products.models import Product, ProductImage

@login_required()
def order_history(request):
    orders_list = Order.objects.filter(user_id=request.user.id).order_by('-created_at') # the - == DESC
    return render(request, 'order_history/order_history.html', context={'orders_list': orders_list})

@login_required()
def get_order_by_id(request, id):
    order = get_object_or_404(Order, pk=id)
    products_list = []
    for obj in OrderDetails.objects.filter(order_id=id):
        products_list.append({'product': obj.product, 'quantity': obj.quantity, 'total_price': obj.product.price*obj.quantity})
    order_price = sum([i['total_price'] for i in products_list])
    return render(request, 'order_history/order_details.html', context={'order': order, 'products_list': products_list, 'order_price': order_price})
