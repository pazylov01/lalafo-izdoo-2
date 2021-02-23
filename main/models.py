from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255)
    priority = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('priority',)    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_lower = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.IntegerField()
    file = models.ImageField(upload_to='img/%Y/%m/%d/')
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_create',)   


# Create your models here.
