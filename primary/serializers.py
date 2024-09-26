from rest_framework import serializers
from primary.models import Category, Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # category_id = CategorySerializer()
    # category_id = serializers.StringRelatedField(read_only=True)
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category_id')
    class Meta:
        model = Product
        # fields = '__all__'
        # fields = ['product_name','category_id', 'sku']
        fields = ['url','id','sku','product_name','product_description','product_price']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    product= ProductSerializer(many = True, read_only = True)
   
    # product_category = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='product_price'
    #  )
    class Meta:
        model = Category
        fields = ['category_name','product']
        # fields ='__all__'




    