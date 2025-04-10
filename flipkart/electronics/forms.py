from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id','name', 'price','description', 'image']

    image = forms.ImageField(label='Image', required=False)