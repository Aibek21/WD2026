from rest_framework import mixins, generics

from api.models import Product
from api.serializers import Product2Serializer


class ProductListAPIView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = Product2Serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailAPIView(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = Product2Serializer
    lookup_url_kwarg = 'product_id'

    def get(self, request, product_id, *args, **kwargs):
        return self.retrieve(request, product_id, *args, **kwargs)

    def put(self, request, product_id, *args, **kwargs):
        return self.update(request, product_id, *args, **kwargs)

    def delete(self, request, product_id, *args, **kwargs):
        return self.destroy(request, product_id, *args, **kwargs)
