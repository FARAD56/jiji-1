from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from jiji.models import product, cart, category, OrderItem, region
from django.contrib import messages
# Create your views here.

def index_page(request):
    query = request.GET.get("q") if request.GET.get("q") != None else ""
    reg = request.GET.get("r") if request.GET.get("r") != None else ""

    products = product.objects.all()
    categories = category.objects.all()
    regions = region.objects.all()

    if query:
        products = products.filter(
            Q(category_id__name=query) | Q(name__icontains=query)
        )
    
    if reg:
        products = products.filter(region_id__name=reg)

    context = {
        'products': products,
        'categories': categories,
        'regions': regions,
        'count': products.count(),
    }
    return render(request, 'shop.html', context)


def detail_page(request, pk):
    item = get_object_or_404(product, id=pk)
    categories = category.objects.all()

    context = {
        "product": item,
        'categories': categories,
    }
    return render(request, "shop-detail.html", context)


def cart_view(request):
    curr_cart = cart.objects.all()
    curr_cart = curr_cart[0] if curr_cart.exists() else cart.objects.create()

    context = {
        "cart": curr_cart
    }
    return render(request, "cart.html", context)



def add_to_cart(request, pk):
    curr_product = get_object_or_404(product, id=pk)
    order_item, created = OrderItem.objects.get_or_create(product=curr_product)

    curr_cart = cart.objects.all()
    curr_cart = curr_cart[0] if curr_cart.exists() else cart.objects.create()
    
    if order_item in curr_cart.order_items.all():
        messages.warning(request, f"{curr_product.name} already in cart")
    else:
        curr_cart.order_items.add(order_item)
        curr_cart.save()
        messages.success(request, f"{curr_product.name} added to cart")

    return redirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, pk):
    curr_product = get_object_or_404(product, id=pk)
    order_item = get_object_or_404(OrderItem, product=curr_product)

    curr_cart = cart.objects.all()
    curr_cart = curr_cart[0] if curr_cart.exists() else cart.objects.create()

    if order_item in curr_cart.order_items.all():
        curr_cart.order_items.remove(order_item)
        curr_cart.save()

    order_item.delete()
    messages.warning(request, f"{curr_product.name} has been removed from cart")

    return redirect(request.META.get('HTTP_REFERER'))


def increase_quantity(request, pk):
    order_item = OrderItem.objects.get(id=pk)
    order_item.quantity += 1
    order_item.save()
    return redirect(request.META.get('HTTP_REFERER'))


def decrease_quantity(request, pk):
    order_item = OrderItem.objects.get(id=pk)
    order_item.quantity -= 1
    if order_item.quantity < 0:
        order_item.quantity = 0
    order_item.save()
    return redirect(request.META.get('HTTP_REFERER'))