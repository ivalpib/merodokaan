from rest_framework import serializers
from primary.models import Category, Product
        
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category_id')
    test = serializers.HyperlinkedIdentityField(view_name = "product-detail")
    class Meta:
        model = Product
        fields = ['id','sku','product_name','product_description','product_price','category','test']


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='product_description',
        source="products"
     )
    class Meta:
        model = Category
        fields = ['url','category_name','product']