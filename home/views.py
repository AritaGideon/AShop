from django.shortcuts import render
from django.http import HttpResponse
from products.forms import ProductSearchForm
from products.models import Categories


def home(request):
    form = ProductSearchForm()
    categories = Categories.objects.all()
    return render(request, 'home/home.html', {'form': form})

