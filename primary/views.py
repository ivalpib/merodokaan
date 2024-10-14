from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout 
from primary.form import UserRegistrationForm
from django.contrib import messages
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.
def HomeView(request):
    return render(request,'index.html')

def LoginView(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
       else:
            # Handle authentication failure
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    elif request.user.is_authenticated:
        messages.success(request, 'You are already logged in.')
        return redirect('index')
    else:
        return render(request, 'login.html')

def LogoutView(request):
    logout(request)
    return redirect('login')

def RegistrationView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('login')
        
    elif request.user.is_authenticated:
        messages.success(request, 'You are already registered')
        return redirect('index')       
    else:
        form = UserRegistrationForm()
    
    return render(request,'registration.html', {'form':form})

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        products = instance.products.all()
        category_data = self.get_serializer(instance, context = {'request':request}).data
        products_data = ProductSerializer(products, many=True, context={'request': request}).data

        return Response({
            'category': category_data,
            'products': products_data
        })

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#function based views
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def testView(request, pk=None):
    if request.method == "GET":
        product = Product.objects.all()
        serializer = ProductSerializer(product, many = True, context = {'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        #require context if there is HyperLinked required
        serializer = ProductSerializer(data=request.data, context={'request':request}) 
        if serializer.is_valid():
            product = serializer.save() 
            return JsonResponse(serializer.data)
    elif request.method in ['PUT','PATCH']:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data = request.data, partial= True, context = {'request': request})
        if serializer.is_valid():
            updated_product = serializer.save()
            return JsonResponse(ProductSerializer(updated_product, context={'request': request}).data)
    elif request.method == 'DELETE':
        product = Product.objects.get(id=pk)
        product.delete()
        return JsonResponse({"message":"Chosen Product has been deleted successfully."}, status=204)
    else:
        return HttpResponse(status=405) 

    # 

