from pprint import pprint
from tracemalloc import get_object_traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from django.http import Http404

from .filters import *

from .models import User, Safety, Report, Brand, Product
from .serializers import (
    UserSerializer,
    SafetySerializer,
    ReportSerializer,
    BrandSerializer,
    ProductSerializer,
)

# Cria a view da lista completa de usuários
class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()  ## Busca os objetos
    serializer_class = UserSerializer
    filter_backends = (FiltroUser,)

# Cria a view do detalhamento (GET, PUT, DELETE) de um único usuário a partir de sua idUser
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'idUser'  ## Marca como chave primária para a url a mesma da entidade
    queryset = User.objects.all()

# Cria a view da lista completa de Safety (perdão pela não tradução)
class SafetyList(generics.ListCreateAPIView):

    queryset = Safety.objects.all()
    serializer_class = UserSerializer
    filter_backends = (FiltroSafety,)

# Cria a view do detalhamento (GET, PUT, DELETE) de uma única safety a partir de sua idSafety
class SafetyDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SafetySerializer
    lookup_field = 'idSafety'
    queryset = Safety.objects.all()

# Cria a view da lista completa de laudos
class ReportList(generics.ListCreateAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = (FiltroReport,)

# Cria a view do detalhamento (GET, PUT, DELETE) de um único laudo a partir de sua idReport
class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    lookup_field = 'idReport'
    queryset = Report.objects.all()

# Cria a view da lista completa de marcas
class BrandList(generics.ListCreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (FiltroBrand,)

# Cria a view do detalhamento (GET, PUT, DELETE) de uma única marca a partir de sua idBrand
class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    lookup_field = 'idBrand'
    queryset = Brand.objects.all()

# Cria a view da lista completa de produtos
class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (FiltroProduct,)

# Cria a view do detalhamento (GET, PUT, DELETE) de um único produto a partir de sua barCode
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'barCode'
    queryset = Product.objects.all()

# View que dado um barCode, retorna um merge da do produto com as tabelas safety, brand e report
class ProductJoinedDetails(APIView):
    
    def get_object(self, entity, pk):
        try:
            target = entity.objects.get(pk=pk)
            return target
        except entity.DoesNotExist:
            raise Http404

    def get(self, request, barCode):

        product = self.get_object(Product, barCode)

        product_serialized = ProductSerializer(product, context={'request': request})
        brand = BrandSerializer(product.idBrand, context={'request': request})        
        safety = SafetySerializer(product.idSafety, context={'request': request})

        test_dict = {**product_serialized.data, **brand.data, **safety.data}

        return Response(test_dict)

        