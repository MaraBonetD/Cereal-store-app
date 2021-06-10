from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from products.models import Product, ProductImage, ProductReview
from products.forms.product_form import ProductCreateForm, ProductUpdateForm
from products.forms.review_form import AddReviewForm
from django.db.models import Avg

# Create your views here.
def index(request):
    products_list = []
    for product in Product.objects.all().order_by('name'):
        products_list.append({
            "id": product.id,
            "image": get_object_or_404(ProductImage, pk=product.id).image,
            "name": product.name,
            "brand":product.brand,
            "price": product.price,
            "description": product.description,
            "on_sale": product.on_sale
        })
    return render(request, 'products/index.html', context={ 'products_list': products_list})

# People can see reviews whithout been logged in, thus we are not using decorator @login_required in here
def get_product_by_id(request, id):
    reviews = ProductReview.objects.filter(product_id=id) # filter(product_id=id)[:10]
    average_rating = ProductReview.objects.filter(product_id=id).aggregate(Avg('rating'))['rating__avg'] # apparently it has to be 2 underscores
    return render(request, 'products/product_details.html', {
        'product': get_object_or_404(Product, pk=id),
        'reviews': reviews,
        'average_rating': average_rating
    })

@login_required
def create_new_product(request):
    if request.method =='POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()
            return redirect('products_index')
    else:
        form = ProductCreateForm()
    return render(request, 'products/create_new_product.html',{
        'form': form
    })

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('products_index')

@login_required
def update_product(request, id):
    instance = get_object_or_404(Product,pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('product_details', id=id)
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, 'products/update_product.html', {
        'form': form,
        'id': id
    })

@login_required
def add_review(request, id):
    if request.method == 'POST':
        form = AddReviewForm(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = get_object_or_404(Product, pk=id)
            review.save()
            return redirect('product_details', id=id) # Or products_index.html
    else:
        form = AddReviewForm()
    return render(request, 'products/add_review.html', {
        'form': form,
        'id': id
    })