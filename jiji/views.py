from django.shortcuts import render
from .models import product,category,region,cart
from .serializers import productSerializer,cartSerializer,regionSerializer,categorySerializer,stockSerializer,createCartSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getResources(request):
    if request.method=='GET':
        products = product.objects.all()
        categories = category.objects.all()
        regions = region.objects.all()

        # Filtering
        category_id = request.GET.get('category_id')
        region_id = request.GET.get('region_id')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        if category_id:
            products = products.filter(category_id=category_id)
        if region_id:
            products = products.filter(region_id=region_id)
        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

        

        serializer = productSerializer(products, many=True)

        category_serializer = categorySerializer(categories, many=True)

        region_serializer = regionSerializer(regions,many=True)
        
        data = {
            'products': serializer.data,
            'categories': category_serializer.data,
            'regions':region_serializer.data
        }        
        return Response(data,  status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_products(request):
    if request.method=='GET':
        products = product.objects.all()

        # Filtering
        category_id = request.GET.get('category_id')
        region_id = request.GET.get('region_id')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        if category_id:
            products = products.filter(category_id=category_id)
        if region_id:
            products = products.filter(region_id=region_id)
        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

        serializer = productSerializer(products, many=True)      
        return Response(serializer.data,  status=status.HTTP_200_OK)


@api_view(['GET'])
def get_categories(request):
    categories = category.objects.all()

    serializer = categorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_regions(request):
    regions = region.objects.all()

    serializer = categorySerializer(regions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getProduct(request,pk):
    if request.method=='GET':
        products = product.objects.get(id=pk)
        serializer = productSerializer(products)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def cartList(request):
    if request.method=='GET':
        carts = cart.objects.all()
        serializer = cartSerializer(carts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
  
    

@api_view(['PATCH','DELETE'])
def updateCart(request,pk):
    if request.method=='PATCH':
        carts = cart.objects.get(id=pk)
        serializer = cartSerializer(carts, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    elif request.method == 'DELETE':
        carts = cart.objects.get(id=pk)
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getStock(request,pk):
    if request.method=='GET':
        products = product.objects.get(id=pk)
        serializer = stockSerializer(products)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def createCart(request):
    if request.method=='POST':
        serializer = createCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response (status=status.HTTP_403_FORBIDDEN)