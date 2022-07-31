from django.http import JsonResponse, HttpResponse

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.foodcards.models import Cards, CardsCategories
from apps.foodcards.serializer import CardsSerializer, CardsCategorySerializer


class PostAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['in_basket']
    serializer_class = CardsSerializer
    search_fields = ['title']
    ordering_fields = ['created_at']
    queryset = Cards.objects.all()

    def post(self, request):
        request_body = request.data
        srz = CardsSerializer(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Cards.objects.get(id=pk)
        except Cards.DoesNotExist:
            return Response({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = CardsSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            product = Cards.objects.get(id=pk)
        except Cards.DoesNotExist:
            return JsonResponse({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class PostCategoriesAPIView(generics.ListAPIView):
    serializer_class = CardsCategorySerializer
    queryset = CardsCategories.objects.all()

    def post(self, request):
        request_body = request.data
        new_product = CardsCategories.objects.create(title=request_body['title'],
                                                       )
        srz = CardsCategorySerializer(new_product, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class PostCategoryRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            category = CardsCategories.objects.get(id=pk)
        except CardsCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = CardsCategorySerializer(category, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            category = Cards.objects.get(id=pk)
        except CardsCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)