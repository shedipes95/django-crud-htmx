from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "sku", "price", "stock"]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "quantity"]

    def clean_quantity(self):
        q = self.cleaned_data["quantity"]
        product = self.cleaned_data.get("product")
        if product and q > product.stock:
            raise forms.ValidationError("Not enough stock.")
        return q