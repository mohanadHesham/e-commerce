from django.shortcuts import render
from .models import Category,Product
# Create your views here.
def home(request):
    allcategory = Category.objects.all()
    allproducts = Product.objects.all()
    return render(request,'pages/home.html',{"allproducts":allproducts,"allcategory":allcategory})

def category(request):
    allcategory = Category.objects.all()
    allproducts = Category.objects.all()
    return render(request,'pages/category.html',{"allproducts":allproducts,"allcategory":allcategory})

def men (request):
    return render (request,'pages/men.html',{
        'men' : Product.objects.filter(category_id=1)
    })

def women (request):
    return render (request,'pages/women.html',{
        'women' : Product.objects.filter(category_id=2)
    })
def child (request):
    return render (request,'pages/child.html',{
        'child' : Product.objects.filter(category_id=3)
    })

def product (request, productid):
    product= Product.objects.get(id=productid)
    return render (request,'pages/product.html',{'product':product})

def newArrival(request):
    allcategory = Category.objects.all()
    allproducts = Product.objects.all().order_by("-id")
    return render(request,'pages/newArrival.html',{"allcategory":allcategory,"allproducts":allproducts})

