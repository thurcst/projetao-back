from http.client import HTTPResponse
from rest_framework import generics
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

# Cria a view da lista completa de usuários
class UserList(APIView):
    def get(self, request):
        user_list = User.objects.all()  ## Busca os objetos

        filters_backends = [DjangoFilterBackend, filters.OrderingFilter]
        ordering_fields = ["idUser"]
        filterset_fields = ["idUser", "nick", "createdAt"]

        serializer = UserSerializer(user_list)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer_class = UserSerializer

    def put(self, request):
        ...

    def delete(self, request):
        return Response(status.HTTP_400_BAD_REQUEST)


# Cria a view do detalhamento (GET, PUT, DELETE) de um único usuário a partir de sua idUser
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = "idUser"  ## Marca como chave primária para a url a mesma da entidade
    queryset = User.objects.all()


# Cria a view da lista completa de Safety (perdão pela não tradução)
class SafetyList(generics.ListCreateAPIView):

    queryset = Safety.objects.all()
    serializer_class = SafetySerializer
    filters_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["idSafety"]
    filterset_fields = ["idSafety", "category", "description"]


# Cria a view do detalhamento (GET, PUT, DELETE) de uma única safety a partir de sua idSafety
class SafetyDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SafetySerializer
    lookup_field = "idSafety"
    queryset = Safety.objects.all()


# Filtro por range de data dos laudos
class ReportDateFilter(filters.FilterSet):

    date_gte = filters.DateFilter(name="date", lookup_expr="gte")
    date_lte = filters.DateFilter(name="date", lookup_expr="lte")

    class Meta:

        model = Report
        fields = ["createdAt"]


# Cria a view da lista completa de laudos
class ReportList(generics.ListCreateAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filters_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["idReport"]
    filterset_fields = ["idReport"]
    filter_class = ReportDateFilter


# Cria a view do detalhamento (GET, PUT, DELETE) de um único laudo a partir de sua idReport
class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    lookup_field = "idReport"
    queryset = Report.objects.all()


# Cria a view da lista completa de marcas
class BrandList(generics.ListCreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filters_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["idBrand"]
    filterset_fields = ["idBrand", "brandName", "contact"]


# Cria a view do detalhamento (GET, PUT, DELETE) de uma única marca a partir de sua idBrand
class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    lookup_field = "idBrand"
    queryset = Brand.objects.all()


# Filtro dos produtos
class ProductDateFilter(filters.FilterSet):

    date_gte = filters.DateFilter(name="date", lookup_expr="gte")
    date_lte = filters.DateFilter(name="date", lookup_expr="lte")

    class Meta:

        model = Product
        fields = ["createdAt"]


# Cria a view da lista completa de produtos
class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filters_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["barCode"]
    filterset_fields = [
        "barCode",
        "idBrand",
        "idSafety",
        "idReport",
        "productName",
        "productCategory",
        "productIngredients",
    ]
    filter_class = ProductDateFilter


# Cria a view do detalhamento (GET, PUT, DELETE) de um único produto a partir de sua barCode
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    lookup_field = "barCode"
    queryset = Product.objects.all()
