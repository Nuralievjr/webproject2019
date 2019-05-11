from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'




class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    count = models.IntegerField()
    image = models.ImageField(upload_to = 'media', default = 'media/404.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    visit = models.IntegerField(default=0)
    description = models.CharField(max_length=400, default='Опсиание еще не добавлено!')

    def inc(self):
        self.visit+=1



class ContactModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.CharField(max_length=200)




