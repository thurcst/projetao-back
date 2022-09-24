from rest_framework import generics
from .models import *
from .serializers import *
from .filters import *


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

