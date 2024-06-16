from .models import product,category,region,cart, OrderItem
from rest_framework import serializers

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id','name']

class regionSerializer(serializers.ModelSerializer):
    class Meta:
        model = region
        fields = ['id','name']


class productSerializer(serializers.ModelSerializer):
    category_id = categorySerializer()
    region_id = regionSerializer()
    class Meta:
        model = product
        fields = ['id','name','description','price','stock_quantity','category_id','region_id']

class OrderItemSerializer(serializers.ModelSerializer):
    product = productSerializer()
    class Meta:
        model = OrderItem
        fields = ["quantity", "date_added", "product"]


class cartSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = cart
        fields = ['order_items']

class stockSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ["name", 'stock_quantity']