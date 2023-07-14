from django.contrib import admin
from .models import DishesType, Dish, Sale
# Register your models here.

admin.site.register(DishesType)
admin.site.register(Dish)
admin.site.register(Sale)
