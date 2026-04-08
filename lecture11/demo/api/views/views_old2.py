import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from api.models import Product, Category
from api.serializers import ProductSerializer, Product2Serializer


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
        serializer = Product2Serializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)

        serializer = Product2Serializer(data=data)
        if serializer.is_valid():
            serializer.save() # create_function will be executed inside of serializer
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Product not found'}, status=404)

    if request.method == 'GET':
        serializer = Product2Serializer(product)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)

        serializer = Product2Serializer(data=data, instance=product)
        if serializer.is_valid():
            serializer.save() # update_function will be executed inside of serializer
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete() # delete from products where id = product_id
        return JsonResponse({'message': 'Product deleted'})
