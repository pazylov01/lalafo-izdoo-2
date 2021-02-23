from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context={
        'categories': categories,
        'products': products
    }
    return render(request, 'main/index.html', context)

def category(request, id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    active = id
    context={
        'categories': categories,
        'products': products,
        'active':active
    }
    return render(request, 'main/category.html', context)


def search(request):
    categories = Category.objects.all()
    products = Product.objects.filter(title_lower__contains=request.GET.get('search'))
    context={
        'categories': categories,
        'products': products,
        'count': products.count()
    }
    return render(request, 'main/search.html', context)

@login_required(login_url='login')
def lk(request):
    personal = User.objects.get(id=request.user.id)
    categories = Category.objects.all()
    context = {
        'personal': personal,
        'categories': categories
    }
    return render (request, 'main/lk.html', context)


def productAdd(request):
    if request.method == 'POST' or request.FILES['file']:
        tl = request.POST['title'].lower()
        Product.objects.create(
            category_id=request.POST['category'],
            user_id=request.user.id,
            title=request.POST['title'],
            title_lower=tl,
            price=request.POST['price'],
            description=request.POST['description'],
            file=request.FILES['file']
        )
        return redirect('lk')


def detail(request,id):
    p = Product.objects.get(id=id)
    context = {
        'p' : p
    }
    return render(request, 'main/detail.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('lk')
    return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

# Create your views here.
