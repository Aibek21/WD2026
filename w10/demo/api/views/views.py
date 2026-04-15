from rest_framework import viewsets

from api.models import Product
from api.serializers import Product2Serializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product2Serializer

    @action(methods=['GET'], detail=False)
    def active(self, request):
        products = Product.objects.filter(is_active=True)
        serializer = Product2Serializer(products, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def not_active(self, request):
        products = Product.objects.filter(is_active=False)
        serializer = Product2Serializer(products, many=True)
        return Response(serializer.data)

