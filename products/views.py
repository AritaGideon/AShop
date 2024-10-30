from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm


def product(request):
    global query
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.all()
    message = None

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

                # If no product is found show "Product not available" message
            if not products.exists():
                message = 'Product not available'
        else:
            message = 'Please enter a valid product name or price'
    else:
        message = 'Invalid input. Please try again.'

    return render(request, 'product.html', {'form': form, 'products': products, 'message': message})
