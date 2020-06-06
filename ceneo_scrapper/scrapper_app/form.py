from django import forms
from django.core.exceptions import ValidationError

from scrapper_app.models import ProductModel


class AddProductForm(forms.ModelForm):
    # product_id = forms.CharField(max_length=8, label='ID produktu')
    class Meta:
        model = ProductModel
        fields = ['product_id', ]

    def clean_product_id(self):
        product_id = self.cleaned_data.get('product_id')
        if len(product_id) != 8:
            raise ValidationError('ID powinno zawierać 8 cyfr.')
