from rest_framework import generics
from django_filters import rest_framework as filters
from .models import User, Safety, Report, Brand, Product
from .serializers import UserSerializer, SafetySerializer, ReportSerializer, BrandSerializer, ProductSerializer


# Cria a view da lista completa de usuários
class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()  ## Busca os objetos
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Cria a view do detalhamento (GET, PUT, DELETE) de um único usuário a partir de sua idUser
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'idUser'  ## Marca como chave primária para a url a mesma da entidade
    queryset = User.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Cria a view da lista completa de Safety (perdão pela não tradução)
class SafetyList(generics.ListCreateAPIView):

    queryset = Safety.objects.all()
    serializer_class = SafetySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Cria a view do detalhamento (GET, PUT, DELETE) de uma única safety a partir de sua idSafety
class SafetyDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SafetySerializer
    lookup_field = 'idSafety'
    queryset = Safety.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Filtro por range de data dos laudos
class ReportDateFilter(filters.FilterSet):

    date_gte = filters.DateFilter(name="date", lookup_expr='gte')
    date_lte = filters.DateFilter(name="date", lookup_expr='lte')

    class Meta:

        model = Report
        fields = ['createdAt', 'expiredAt']

# Cria a view da lista completa de laudos
class ReportList(generics.ListCreateAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Cria a view do detalhamento (GET, PUT, DELETE) de um único laudo a partir de sua idReport
class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    lookup_field = 'idReport'
    queryset = Report.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Cria a view da lista completa de marcas
class BrandList(generics.ListCreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Cria a view do detalhamento (GET, PUT, DELETE) de uma única marca a partir de sua idBrand
class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    lookup_field = 'idBrand'
    queryset = Brand.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Filtro por data dos produtos
class ProductDateFilter(filters.FilterSet):

    date = filters.DateFilter(name="date")

    class Meta:

        model = Product
        fields = ['createdAt']

# Cria a view da lista completa de produtos
class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Cria a view do detalhamento (GET, PUT, DELETE) de um único produto a partir de sua barCode
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'barCode'
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

