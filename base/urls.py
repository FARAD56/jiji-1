from django.urls import path
from . views import index_page, detail_page, add_to_cart, remove_from_cart, cart_view, increase_quantity, decrease_quantity

urlpatterns = [
    path("", index_page, name="index-page"),
    path("detail/<pk>/", detail_page, name="detail-page"),
    path("add-to-cart/<pk>/", add_to_cart, name="add-to-cart"),
    path("remove-from-cart/<pk>/", remove_from_cart, name="remove-from-cart"),
    path("cart-view/", cart_view, name="cart-view"),
    path("increase-quantity/<pk>/", increase_quantity, name="increase-quantity"),
    path("decrease-quantity/<pk>/", decrease_quantity, name="decrease-quantity"),
]