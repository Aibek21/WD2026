from django.urls import path

from api.views import views
from rest_framework import routers

urlpatterns = [
    # path('categories/', views.category_list),
    # path('categories/<int:category_id>/products/', views.category_products),
    # path('products/', views.product_list),
    # path('products/<int:product_id>/', views.product_detail),
    # path('products/', views.ProductListAPIView.as_view()),
    # path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
]


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
urlpatterns += router.urls
