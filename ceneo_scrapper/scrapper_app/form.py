import re

from django import forms
from django.core.exceptions import ValidationError

from scrapper_app.models import ProductModel


class AddProductForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = ('product_id', )

    def clean_product_id(self):
        product_id = self.cleaned_data.get('product_id')
        if len(product_id) > 8:
            raise ValidationError('ID produktu zawiera maksymalnie 8 znaków.')
        if re.findall(r'[^\d]+', product_id):
            raise ValidationError('ID powinno zawierać tylko cyfry.')
        return product_id

