from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from search.models import Search
from products.models import Product, ProductImage


def get_search(request):
    #class Meta:
        #abstract=True
    if 'search_string' in request.GET:
        search_string = request.GET['search_string']
    else:
        return HttpResponseNotFound("<h1> Search does not match any product</h1>")
    search_product = Product.objects.filter(name__icontains=search_string)
    search_instance = Search()
    search_instance.user = request.user
    search_instance.search_string = search_string
    search_instance.save()
    products_images = ProductImage.objects.all()
    search_products_return = []
    for product in search_product:
        search_products_return.append({
            "image": [image for image in products_images if product.id==image.product_id][0].image,
            "id": product.id,
            "name": product.name,
            "brand": product.brand,
            "price": product.price,
            "description": product.description,
            "on_sale": product.on_sale
        })
    return render(request, 'search/search_product.html', context={'search_products_return': search_products_return, 'search_string': request.GET['search_string']})


