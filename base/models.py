from django.db import models

class DishesType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Dish(models.Model):
    title = models.CharField(max_length=50)
    dishesType = models.ForeignKey(DishesType, on_delete=models.SET_NULL, null=True)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    picture = models.ImageField(upload_to='files/picturesDishes')
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title
    
class Sale(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='sales')
    date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return f"{self.dish} - {self.date}"
    

    
