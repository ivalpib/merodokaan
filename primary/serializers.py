from rest_framework import serializers
from primary.models import Category, Product



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # product = ProductSerializer(many = True, read_only = True, source = 'product_category')
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    cat_id = CategorySerializer(read_only = True)
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['url','id','sku','product_name','product_description','product_price']


    