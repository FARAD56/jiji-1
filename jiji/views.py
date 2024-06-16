from django.shortcuts import render, get_object_or_404
from .models import product,category,region,cart, OrderItem
from .serializers import productSerializer,cartSerializer,regionSerializer,categorySerializer,stockSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_all_products(request):
    products = product.objects.all()
    serializer = productSerializer(products, many=True)      

    return Response(serializer.data)


@api_view(['GET'])
def get_category_products(request, id):
    products = product.objects.filter(category_id__id = id)
    serializer = productSerializer(products, many=True)      

    return Response(serializer.data)


@api_view(['GET'])
def get_categories(request):
    categories = category.objects.all()
    serializer = categorySerializer(categories, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_regions(request):
    regions = region.objects.all()
    serializer = categorySerializer(regions, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    products = product.objects.get(id=pk)
    serializer = productSerializer(products)
    return Response(serializer.data)

    
@api_view(['GET'])
def cartList(request):
    carts = cart.objects.all()
    serializer = cartSerializer(carts,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_to_cart(request, pk):
    item = get_object_or_404(product, id=pk)
    order_item, created = OrderItem.objects.get_or_create(product=item)

    curr_cart = cart.objects.all()
    if curr_cart.exists():
        curr_cart = curr_cart[0]

    if order_item not in curr_cart.order_items.all():
        curr_cart.order_items.add(order_item)
        curr_cart.save()

    serializer = cartSerializer(curr_cart)
    return Response(serializer.data)


@api_view(['DELETE'])
def remove_from_cart(request, pk):
    item = get_object_or_404(product, id=pk)
    order_item, created = OrderItem.objects.get_or_create(product=item)
    curr_cart = cart.objects.all()

    if curr_cart.exists():
        curr_cart = curr_cart[0]

    if order_item not in curr_cart.order_items.all():
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    curr_cart.order_items.remove(order_item)
    curr_cart.save()
    order_item.delete()
    serializer = cartSerializer(curr_cart)
    return Response(serializer.data)


@api_view(['GET'])
def getStock(request,pk):
    products = product.objects.get(id=pk)
    serializer = stockSerializer(products)
    return Response(serializer.data)