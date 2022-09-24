from multiprocessing import context
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Safety, Report, Brand, Product
from .serializers import (
    UserSerializer,
    SafetySerializer,
    ReportSerializer,
    BrandSerializer,
    ProductSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from django.shortcuts import get_object_or_404

from rest_framework import generics

from pprint import pprint

# Cria a view da lista completa de usuários
class UserList(APIView):
    def get(self, request):
        user_list = User.objects.all()  ## Busca os objetos
        pprint(list(user_list))
        serializer = UserSerializer(user_list, many=True)
        pprint(serializer.data)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)


# Cria a view do detalhamento (GET, PUT, DELETE) de um único usuário a partir de sua idUser
class UserDetail(APIView):
    def get_object(self, idUser):
        try:
            return User.objects.get(idUser)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, idUser):
        user = self.get_object(idUser)
        serializer = UserSerializer(user)
        return Response(data=serializer.data)

    def post(self, request):
        serializer_class = UserSerializer
        serialized = serializer_class(request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(status.HTTP_201_CREATED)
        return Response(data=serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, idUser):
        target = self.get_object(idUser)

        serializer = UserSerializer(target, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, idUser):
        target = self.get_object(idUser)
        try:
            target.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Cria a view da lista completa de Safety (perdão pela não tradução)
class SafetyList(APIView):
    def get(self, request):
        safety_list = Safety.objects.all()
        filters_backends = [DjangoFilterBackend, filters.OrderingFilter]
        ordering_fields = ["idSafety"]
        filterset_fields = ["idSafety", "category", "description"]

        serializer = SafetySerializer(safety_list, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)


# Cria a view do detalhamento (GET, PUT, DELETE) de uma única safety a partir de sua idSafety
class SafetyDetail(APIView):
    def get_object(self, pk):
        try:
            return Safety.objects.get(pk)
        except Safety.DoesNotExist:
            raise Http404

    def get(self, pk):
        safety = self.get_object(pk)
        serializer = SafetySerializer(safety)
        return Response(serializer.data)

    def post(self, request):
        serializer_class = SafetySerializer
        serialized = serializer_class(request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(status.HTTP_201_CREATED)
        return Response(serialized.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        safety = self.get_object(pk)
        serializer = SafetySerializer(safety, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        safety = self.get_object(pk)
        safety.delete()
        return Response(status.HTTP_204_NO_CONTENT)


# Filtro por range de data dos laudos
class ReportDateFilter(filters.FilterSet):

    date_gte = filters.DateFilter(name="date", lookup_expr="gte")
    date_lte = filters.DateFilter(name="date", lookup_expr="lte")

    class Meta:

        model = Report
        fields = ["createdAt"]


# Cria a view da lista completa de laudos
class ReportList(APIView):
    def get(self, request):
        report_list = Report.objects.all()  ## Busca os objetos
        serializer = ReportSerializer(
            report_list, many=True, context={"request": request}
        )

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self):
        return Response(status.HTTP_400_BAD_REQUEST)

    def put(self):
        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self):
        return Response(status.HTTP_400_BAD_REQUEST)


# Cria a view do detalhamento (GET, PUT, DELETE) de um único laudo a partir de sua idReport
class ReportDetail(APIView):
    def get_object(self, idReport):
        try:
            return Report.objects.get(pk=idReport)
        except Report.DoesNotExist:
            raise Http404

    def get(self, request, idReport):
        pprint(idReport)
        report = self.get_object(idReport)

        serializer = ReportSerializer(report, context={"request": request})
        return Response(data=serializer.data)

    def post(self, request):
        serializer_class = ReportSerializer
        serialized = serializer_class(request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(status.HTTP_201_CREATED)
        return Response(data=serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, idReport):
        target = self.get_object(idReport)

        serializer = ReportSerializer(target, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, idReport):
        target = self.get_object(idReport)
        try:
            target.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Cria a view da lista completa de marcas
class BrandList(APIView):
    def get(self, request):
        brand_list = Brand.objects.all()  ## Busca os objetos

        # TODO: Corrigir sistema de filtros para o GET

        filters_backends = [DjangoFilterBackend, filters.OrderingFilter]

        ordering_fields = ["idBrand"]
        filterset_fields = ["idBrand", "brandName", "contact"]

        serializer = BrandSerializer(
            brand_list, many=True, context={"request": request}
        )

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)


# Cria a view do detalhamento (GET, PUT, DELETE) de uma única marca a partir de sua idBrand
class BrandDetail(APIView):
    def get_object(self, idBrand):
        try:
            return Brand.objects.get(pk=idBrand)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, idBrand):
        brand = self.get_object(idBrand)
        serializer = BrandSerializer(brand, context={"request": request})
        return Response(data=serializer.data)

    def post(self, request):
        serializer_class = BrandSerializer
        serialized = serializer_class(request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(status.HTTP_201_CREATED)
        return Response(data=serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, idBrand):
        target = self.get_object(idBrand)

        serializer = BrandSerializer(target, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, idBrand):
        target = self.get_object(idBrand)
        try:
            target.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Filtro dos produtos
class ProductDateFilter(filters.FilterSet):

    date_gte = filters.DateFilter(name="date", lookup_expr="gte")
    date_lte = filters.DateFilter(name="date", lookup_expr="lte")

    class Meta:

        model = Product
        fields = ["createdAt"]


# Cria a view da lista completa de produtos
class ProductList(APIView):
    def get(self, request):
        product_list = Product.objects.all()
        serializer = ProductSerializer(
            product_list, many=True, context={"request": request}
        )

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)


# Cria a view do detalhamento (GET, PUT, DELETE) de um único produto a partir de sua barCode
class ProductDetail(APIView):
    def get_object(self, barCode):
        try:
            product = Product.objects.get(pk=barCode)
            pprint(product)
            return product
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, barCode):
        product = self.get_object(barCode)
        print(product)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(data=serializer.data)

    def post(self, request):
        serializer_class = ProductSerializer
        serialized = serializer_class(request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(status.HTTP_201_CREATED)
        return Response(data=serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, barCode):
        target = self.get_object(barCode)

        serializer = ProductSerializer(target, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, barCode):
        target = self.get_object(barCode)
        try:
            target.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
