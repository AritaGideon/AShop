from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm


def index(request):
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            # Filter by name (case-insensitive) or price (exact match if it's a valid number)
            try:
                price_query = float(query)
                products = products.filter(Q(name__icontains=query) | Q(price__exact=price_query))
            except ValueError:
                # If query is not a number, search only by name
                products = products.filter(name__icontains=query)

    return render(request, 'index.html', {'form': form, 'products': products})


def new(request):
    return HttpResponse('Create new Product')
