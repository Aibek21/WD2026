import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from api.models import Product, Category


def category_list(request):
    categories = Category.objects.all()  # select * from categories
    categories_json = [c.to_json() for c in categories]
    return JsonResponse(categories_json, safe=False)


def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all()
    products_json = [p.to_json() for p in products]
    return JsonResponse(products_json, safe=False)


# CRUD = create, read, update, delete

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_json = [p.to_json() for p in products]
        return JsonResponse(products_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        # product = Product.objects.create(name=data['name'], price=data['price'], description=data['description'], category_id=data['category_id'])
        product = Product.objects.create(**data)
        return JsonResponse(product.to_json(), status=201)


@csrf_exempt
def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Product not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse(product.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        product.name = data['name']
        product.price = data['price']
        product.description = data['description']
        product.category_id = data['category_id']
        product.save()
        return JsonResponse(product.to_json())
    elif request.method == 'DELETE':
        product.delete() # delete from products where id = product_id
        return JsonResponse({'message': 'Product deleted'})
