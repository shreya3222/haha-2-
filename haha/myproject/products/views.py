from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product, Review
from .forms import ProductForm, ReviewForm

def is_manufacturer(user):
    return user.user_type == 'manufacturer'

@login_required
@user_passes_test(is_manufacturer)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.manufacturer = request.user
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ReviewForm()
    return render(request, 'products/add_review.html', {'form': form, 'product': product})

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.review_set.all()
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})