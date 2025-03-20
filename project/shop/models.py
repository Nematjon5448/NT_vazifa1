from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/image/', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if not self.parent:
            return self.name
        return f"{self.parent.name}: {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    def get_image(self):
        images = self.images.all()
        if images:
            return images[0].image.url
        return "https://salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled.png"

    def get_price(self):
        if self.discount > 0:
            return self.price - self.price * self.discount / 100
        return self.price

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.product.name

class Comment(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}"

class Promotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=150)
    text = models.CharField(max_length=300)
    image = models.ImageField(upload_to='promotion/image', null=True, blank=True)




