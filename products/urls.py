from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='products home'),
    path('new/', views.new, name='New product'),

]
