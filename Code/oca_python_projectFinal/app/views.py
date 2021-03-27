# from django.shortcuts import render
from django.shortcuts import render, redirect
from app.forms import ProductForm
from app.models import Product
# Create your views here.

from django.http import HttpResponse
from .resources import ProductResource
from tablib import Dataset
# from .models import Product

#for auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def signout(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/admin')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/admin')
        else:
            return render(request, 'app/Admin/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'app/Admin/signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'app/Admin/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'app/Admin/signin.html', {'form': form})
def index(request):
        products = Product.objects.all()
        return render(request,'app/welcome.html' , {'products': products})

def admin(request):
    if not request.user.is_authenticated:
    # return render(request,'app/welcome.html')
         return render(request, 'app/Admin/signin.html')
    else :
        return render(request, 'app/Admin/index.html')


def about(request):
    return render(request, 'app/about.html')
    
def gallery(request):
    return render(request, 'app/gallery.html')

def datatable(request):
    if not request.user.is_authenticated:
        return render(request, 'app/Admin/signin.html')
    else :
        return render(request, 'app/Admin/datatable.html')


def formdatatable(request):
    if not request.user.is_authenticated:
        return render(request, 'app/Admin/signin.html')
    else :
        return render(request, 'app/Admin/formdatatable.html')

def editdatatable(request):
    if not request.user.is_authenticated:
        return render(request, 'app/Admin/signin.html')
    else :
        return render(request, 'app/Admin/editdatatable.html')


# Create your views here.
def emp(request):
    if not request.user.is_authenticated:
        return render(request, 'app/Admin/signin.html')
    else :
     if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
     else:
        form = ProductForm()
     return render(request, 'app/Admin/formdatatable.html', {'form': form})


def show(request):
    if not request.user.is_authenticated:
        return render(request, 'app/Admin/signin.html')
    else :
     products = Product.objects.all()
     return render(request, "app/Admin/datatable.html", {'products': products})


def edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'app/Admin/signin.html')
    else :
         product = Product.objects.get(id=id)
         return render(request, 'app/Admin/editdatatable.html', {'product': product})


def update(request, id):
    if not request.user.is_authenticated:
        return render(request, 'app/Admin/signin.html')
    else :
        product = Product.objects.get(id=id)
        form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'app/Admin/datatable.html', {'product': product})


def destroy(request, id):
    if not request.user.is_authenticated:
        return render(request, 'app/Admin/signin.html')
    else :
     product = Product.objects.get(id=id)
     product.delete()
     return redirect("/show")


def single(request, id):
         product = Product.objects.get(id=id)
         return render(request, 'app/blog-details.html', {'product': product})

def simple_upload(request):
    if not request.user.is_authenticated:
        return render(request, 'app/Admin/signin.html')
    else :
     if request.method == 'POST':
        product_resource = ProductResource()
        dataset = Dataset()
        new_products = request.FILES['myfile']
    
        imported_data = dataset.load(new_products.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	form = Product(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3],
        		 data[4],
        		 data[5],
        		)
        	form.save()       

    # return render(request, 'app/Admin/datatable.html')
    products = Product.objects.all()
    return render(request, "app/Admin/datatable.html", {'products': products})

 

