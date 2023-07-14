from django.forms import ModelForm
from .models import Dish,Sale

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'
        
class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'