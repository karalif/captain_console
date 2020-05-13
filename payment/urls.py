from django.urls import path
from . import views

urlpatterns = [
    path('billing/', views.billing_info, name="payment-billing_address")
]