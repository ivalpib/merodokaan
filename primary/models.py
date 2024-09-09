from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=30)

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField(unique=True)
    contact_address = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

class Product(models.Model):
    sku = models.CharField(max_length=15)
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=200)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=12, decimal_places=2)

class PurchaseOrder(models.Model):
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=15)
    po_date_created = models.DateField(auto_now_add=True)
    po_date_received = models.DateField(auto_now=True)

class PurchaseOrderItems(models.Model):
    po_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)

class ProductInventory(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

class SalesOrder(models.Model):
    ...

class SalesOrderItems(models.Model):
    ...



