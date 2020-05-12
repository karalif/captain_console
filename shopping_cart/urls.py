from django.urls import path
from . import views

urlpatterns =[
    path('', views.my_cart, name='my_cart'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:id>', views.delete_from_cart, name='delete_from_cart')
]