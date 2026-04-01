from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Product
from api.serializers import Product2Serializer


class ProductListAPIView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = Product2Serializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Product2Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # create_function will be executed inside of serializer
        return Response(serializer.data, status=201)


class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_id):
        product = self.get_object(pk=product_id)
        serializer = Product2Serializer(product)
        return Response(serializer.data)

    def put(self, request, product_id):
        product = self.get_object(pk=product_id)
        serializer = Product2Serializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, product_id):
        product = self.get_object(pk=product_id)
        product.delete()
        return Response(status=204)
