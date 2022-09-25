from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.views.generic import DetailView
# Create your views here.
# def home(request):
#     return HttpResponse('Home page FOr ecommerce')

def home(request):
    products = Product.objects.all().filter(is_available=True)
    context={
        'products':products
    }
    return render(request,'home/home.html',context)




def about(request):
    return render(request,'home/about.html')

class ProductDetailView(DetailView):
    model = Product