from django.urls import path
from . import views

urlpatterns = [
    path('resources/', views.getResources ),
    path('products/', views.get_all_products ),
    path('categories/', views.get_categories ),
    path('regions/', views.get_regions ),
    path('products/<int:pk>/', views.getProduct ),
    path('carts/', views.cartList ),
    path('carts/<int:pk>/', views.updateCart ),
    path('quantity/<int:pk>/', views.getStock ),
    path('addcart/', views.createCart ),
]