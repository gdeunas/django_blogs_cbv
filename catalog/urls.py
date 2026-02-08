from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products_list/', views.products_list, name='products_list'),

]
