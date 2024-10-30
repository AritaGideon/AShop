from django import forms


class ProductSearchForm(forms.Form):
    query = forms.CharField(max_length=30, required=False, widget=forms.TextInput
    (attrs={'placeholder': 'Search', 'Class': 'form-control me-2'}))
