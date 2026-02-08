from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    # Выбираем 5 последних продуктов
    latest_products = Product.objects.order_by('-id')[:5]

    # Выводим их в консоль
    print('Вывод 5 последних продуктов:')
    for product in latest_products:
        print(f"id: {product.id}, Название: {product.name}, цена за покупку: {product.price}")

    return render(request, 'catalog/home.html', {'products': latest_products})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context=context)


def products_list(requests):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(requests, 'catalog/products_list.html', context=context)
