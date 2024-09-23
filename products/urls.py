from django.urls import path
from . import views

app_name = 'products'  # Namespacing the app

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('compare/', views.compare_products, name='compare_products'),
]
