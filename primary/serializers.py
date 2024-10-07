from rest_framework import serializers
from primary.models import Category, Product


        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
# Foreign Key Relationship:
# In a one-to-many relationship, the table that contains the foreign key 
# (the "many" side) often uses related_name to specify how the related
#  objects can be accessed from the "one" side.

# Primary Key (Foreign Key):
# The table that has the primary key (the "one" side) does not need a 
# related_name because it can be referenced directly using the foreign
# key field name with _id appended (e.g., category_id).

    # No need for many=True because a product has one category instance

# category_id = CategorySerializer()
    # category_id = serializers.StringRelatedField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category_id')
    test = serializers.HyperlinkedIdentityField(view_name = "product-detail")
    # category = CategorySerializer(read_only=True,source ='category_id')
    class Meta:
        model = Product
        # fields = '__all__'
        # fields = ['product_name','category', 'sku']
        fields = ['id','sku','product_name','product_description','product_price','category','test']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    #use source = '' if you want variable name to be different than related_name
    # else won't need to use source = '' if used same related_name as a variable name
    # need to add many=True if there is multiple instances
    # products = serializers.HyperlinkedRelatedField(queryset = Product.objects.select_related('category_id'), many = True, view_name='product-detail') 
    product = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='product_description',
        source="products"
     )
    # product = ProductSerializer(many=True)
    # product_category = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='product_price'
    #  )
    class Meta:
        model = Category
        fields = ['url','category_name','product']
        # fields = '__all__'
    