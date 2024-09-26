from django import forms

from products.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=300)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    available = forms.BooleanField(initial=True, label="Disponible", required=False)
    photo = forms.ImageField(label="Foto", required=False)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data.get("name"),
            description=self.cleaned_data.get("description"),
            price=self.cleaned_data.get("price"),
            available=self.cleaned_data.get("available"),
            photo=self.cleaned_data.get("photo"),
        )
