from django import forms

from .models import Add_Product


class Add_ProductForm(forms.ModelForm):
    class Meta:
        model = Add_Product
        # fields='__all__'
        fields = ['product_category', 'product_name', 'product_price',
                  'sale_price', 'product_img', 'details']
