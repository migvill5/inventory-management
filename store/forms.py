from django import forms
from django.db.models import fields

from .models import (
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery,
    Location,
    Fabricant,
    Category,
    Supplier
)


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'address',
            'email'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'data-val': 'true',
                'data-val-required': 'Please enter name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'data-val': 'true',
                'data-val-required': 'Please enter email',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'address',
                'data-val': 'true',
                'data-val-required': 'Please enter address',
            }),
        }


class BuyerForm(forms.ModelForm):

    class Meta:
        model = Buyer
        fields = [
            'name',
            'address',
            'email'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'data-val': 'true',
                'data-val-required': 'Please enter name',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'address',
                'data-val': 'true',
                'data-val-required': 'Please enter address',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'data-val': 'true',
                'data-val-required': 'Please enter email',
            }),
        }


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            })
        }


class DropForm(forms.ModelForm):
    class Meta:
        model = Drop
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            })
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'code',
            'name',
            'dosage',
            'regsan',
            'available_quantity',
            'min_quantity',
            'category',
            'location',
            'fabricant'
        ]

        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'code',
                'placeholder': 'Barcode'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Product Name'
            }),
            'dosage': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'dosage',
                'placeholder': 'Dosage info.'
            }),
            'regsan': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'regsan',
                'placeholder': 'Sanitary code'
            }),
            'available_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'available_quantity',
                'value': '0'
            }),
            'min_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'min_quantity',
                'value': '0'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'id': 'category'
            }),
            'location': forms.Select(attrs={
                'class': 'form-control',
                'id': 'location'
            }),
            'fabricant': forms.Select(attrs={
                'class': 'form-control',
                'id': 'fabricant'
            }),
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Location name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'description',
                'placeholder': 'Location description'
            }),
        }


class FabricantForm(forms.ModelForm):
    class Meta:
        model = Fabricant
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Fabricant name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'description',
                'placeholder': 'Fabricant description'
            }),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Category name'
            })
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'supplier', 'product', 'design', 'color', 'buyer', 'season', 'drop'
        ]

        widgets = {
            'supplier': forms.Select(attrs={
                'class': 'form-control', 'id': 'supplier'
            }),
            'product': forms.Select(attrs={
                'class': 'form-control', 'id': 'product'
            }),
            'design': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'design'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'color'
            }),
            'buyer': forms.Select(attrs={
                'class': 'form-control', 'id': 'buyer'
            }),
            'season': forms.Select(attrs={
                'class': 'form-control', 'id': 'season'
            }),
            'drop': forms.Select(attrs={
                'class': 'form-control', 'id': 'drop'
            }),
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'order': forms.Select(attrs={
                'class': 'form-control', 'id': 'order'
            }),
            'courier_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'courier_name'
            }),
        }
