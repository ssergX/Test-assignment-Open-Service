from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['patch'])
    def reduce_quantity(self, request, pk=None):
        product = self.get_object()
        amount = request.data.get('amount')

        if amount is None:
            return Response({'error': 'Не указан параметр amount'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            amount = int(amount)
            if amount <= 0:
                return Response({'error': 'amount должен быть положительным числом'},
                                status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'error': 'amount должен быть числом'}, status=status.HTTP_400_BAD_REQUEST)

        if product.quantity >= amount:
            product.quantity -= amount
            product.save()
            return Response({'status': f'количество товара, оствашиеся на складе {product.quantity}',
                             'new_quantity': product.quantity},
                            status=status.HTTP_200_OK)

        return Response({'error': 'не удалось уменьшить количество'}, status=status.HTTP_400_BAD_REQUEST)
