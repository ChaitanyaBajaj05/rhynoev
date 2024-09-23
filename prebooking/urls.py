from django.urls import path
from .views import pre_book, paypal_success, paypal_cancel

urlpatterns = [
    path('', pre_book, name='pre_book'),
    path('paypal/success/', paypal_success, name='paypal_success'),
    path('paypal/cancel/', paypal_cancel, name='paypal_cancel'),
]
