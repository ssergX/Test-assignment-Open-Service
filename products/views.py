from rest_framework import viewsets
from .models import Product, ProductType, Price
from .serializers import ProductSerializer, ProductTypeSerializer, PriceSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['patch'])
    def reduce_quantity(self, request, pk=None):
        product = self.get_object()
        amount = int(request.data.get('amount', 1))
        if product.quantity >= amount:
            product.quantity -= amount
            product.save()
            return Response({'status': f'количество уменьшено на {amount}'}, status=status.HTTP_200_OK)
        return Response({'error': 'не удалось уменьшить количество'}, status=status.HTTP_400_BAD_REQUEST)
