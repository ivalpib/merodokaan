from rest_framework import serializers
from primary.models import Category, Product

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['cat_name']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    cat_id = CategorySerializer()
    class Meta:
        model = Product
        fields = ['sku','product_name','product_description','product_price','cat_id']

    