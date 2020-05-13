from django.urls import path
from . import views

urlpatterns = [
    path('billing/', views.billing_info, name="payment-billing_address"),
    path('payment_info', views.payment_info, name='payment-payment_info')
]