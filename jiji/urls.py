from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_all_products ),
    path('products/categories/<id>/', views.get_category_products),
    path('categories/', views.get_categories ),
    path('regions/', views.get_regions ),
    path('products/<int:pk>/', views.getProduct ),
    path('carts/', views.cartList ),
    path('carts/remove-product/<pk>/', views.remove_from_cart ),
    path('carts/add-product/<pk>/', views.add_to_cart ),
    path('products/stock/<int:pk>/', views.getStock ),
]