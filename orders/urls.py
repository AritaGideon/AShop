from django.urls import path
from . import views


urlpatterns = [
    path('', views.orders, name='home'),
    path('new/', views.new_order, name='new order'),

]

