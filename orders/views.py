from django.http import HttpResponse
from django.shortcuts import render


def orders(request):
    return HttpResponse('Your orders')


def new_order(request):
    return HttpResponse('Make a New Order')


