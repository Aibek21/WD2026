from rest_framework import viewsets

from api.models import Product
from api.serializers import Product2Serializer
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


class ProductPageNumberPagination(PageNumberPagination):
    page_size = 2


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product2Serializer
    permission_classes = [IsAuthenticated]
    # pagination_class = LimitOffsetPagination

    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def active(self, request):
        self.pagination_class = ProductPageNumberPagination
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def not_active(self, request):
        products = Product.objects.filter(is_active=False)
        serializer = Product2Serializer(products, many=True)
        return Response(serializer.data)

