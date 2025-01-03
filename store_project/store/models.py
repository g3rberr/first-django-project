from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    info = models.TextField(blank=True)
    price = models.IntegerField()
    categories = models.ManyToManyField('Category', blank=True, related_name='products')
    image = models.ImageField(upload_to='images/', default='images/default_image.png')
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'pk': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse(
            'category_url',
            kwargs={
                'pk': self.pk
                }      
            )
    
    def __str__(self):
        return self.name
    
    
    
class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name