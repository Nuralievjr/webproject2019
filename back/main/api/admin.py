from django.contrib import admin
from api.models import Category,Product,ContactModel
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ContactModel)