from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Product
from api.serializers import Product2Serializer


# function based view

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = Product2Serializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Product2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # create_function will be executed inside of serializer
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'message': 'Product not found'}, status=404)

    if request.method == 'GET':
        serializer = Product2Serializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Product2Serializer(data=request.data, instance=product)
        if serializer.is_valid():
            serializer.save()  # update_function will be executed inside of serializer
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()  # delete from products where id = product_id
        return Response({'message': 'Product deleted'})