from .models import product,category,region,cart
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


class cartSerializer(serializers.ModelSerializer):
    product_id = productSerializer()
    class Meta:
        model = cart
        fields = ['id','product_id','quantity']

class createCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = ['id','product_id','quantity']       

class stockSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['stock_quantity']