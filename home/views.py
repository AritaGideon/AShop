from django.shortcuts import render
from django.http import HttpResponse
from products.forms import ProductSearchForm


def home(request):
    form = ProductSearchForm()
    return render(request, 'home/home.html', {'form': form})


