from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializer import ProductSerializer
from user.permissions import IsActive


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActive]
