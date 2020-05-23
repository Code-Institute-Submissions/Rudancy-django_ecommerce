from django.shortcuts import render
from products.models import Product

def do_search(request):
    products=Product.objects.filter(name__icontains=request.GET['q'])
    if products is None:
        return render(request, "inde.html")
    else:
        return render(request, "products.html", {"products":products})

# Create your views here.
