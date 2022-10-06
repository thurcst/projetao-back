from asyncore import write
from pprint import pprint
from tracemalloc import get_object_traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from django.http import Http404

import os.path, os
from .filters import *

from .models import User, Safety, Report, Brand, Product
from .serializers import (
    UserSerializer,
    SafetySerializer,
    ReportSerializer,
    BrandSerializer,
    ProductSerializer,
)

def write_barcode(barcode:str) -> bool:
    # Escreve o código de barras no txt se ele já não estiver lá
    dirpath = os.path.abspath('/ScrapperData')
    filepath = os.path.join(dirpath,'sysargs')

    # Cria o diretório se ele não existe
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    
    # Cria o arquivo se ele não existe
    if not os.path.exists(filepath):
        with open(filepath, "w+"): 
            pass

    # Escreve no txt
    with open(filepath,'r+') as file:
        write_in_file = barcode not in file.read()
        if write_in_file:
            file.write(barcode + '\n')

        return write_in_file

def get_product_object_or_404(entity,barcode:str):
    try:
        target = entity.objects.get(pk=barcode)
        return target
    except entity.DoesNotExist:
        write_barcode(barcode) # Se não estiver rodando da vm, comentar essa linha
        raise Http404

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
    serializer_class = SafetySerializer
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
        return get_product_object_or_404(entity,pk)

    def get(self, request, barCode):

        product = self.get_object(Product, barCode)

        product_serialized = ProductSerializer(product, context={'request': request})
        brand = BrandSerializer(product.idBrand, context={'request': request})        
        safety = SafetySerializer(product.idSafety, context={'request': request})

        test_dict = {**product_serialized.data, **brand.data, **safety.data}

        return Response(test_dict)

        