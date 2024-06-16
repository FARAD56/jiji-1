from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
    def get_category_count(self):
        return product.objects.filter(category_id=self).count()
    

class region(models.Model):
    name = models.CharField(max_length=500)

    def get_region_count(self):
        return product.objects.filter(region_id=self).count()

    def __str__(self):
        return self.name
    

class product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images", null=True, blank=True)
    stock_quantity = models.IntegerField()
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    region_id = models.ForeignKey(region, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def exists_in_cart(self):
        return OrderItem.objects.filter(product=self).exists()

    
class OrderItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        return round(self.quantity * self.product.price, 2)

    def __str__(self):
        return f"OrderItem - {self.product.name}"

class cart(models.Model):
    order_items = models.ManyToManyField(to=OrderItem)

    def get_total(self):
        total = 0
        for item in self.order_items.all():
            total += (item.product.price) * item.quantity
        return round(total, 2)

    def __str__(self):
        return "Cart"

    