from django.shortcuts import render
from .models import Products
# Create your views here.


def viewproducts(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, "products/products.html", context)
