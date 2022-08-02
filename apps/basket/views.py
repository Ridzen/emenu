from django.http import JsonResponse, HttpResponse

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.basket.models import Basket
from apps.basket.serializer import BasketSerializer


class BasketAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = BasketSerializer
    search_fields = ['title']
    ordering_fields = ['created_at']
    queryset = Basket.objects.all()

    def post(self, request):
        request_body = request.data
        srz = BasketSerializer(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST)


class BasketRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Basket.objects.get(id=pk)
        except Basket.DoesNotExist:
            return Response({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = BasketSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            product = Basket.objects.get(id=pk)
        except Basket.DoesNotExist:
            return JsonResponse({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

