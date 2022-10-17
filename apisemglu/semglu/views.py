from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

# from django.http import HttpResponse, HttpResponseForbidden

from .filters import *
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from .models import (
    Safety,
    Report,
    Brand,
    Product,
    Review,
)
from .serializers import (
    SafetySerializer,
    ReportSerializer,
    BrandSerializer,
    ProductSerializer,
    ReviewSerializer,
)

from django.http import Http404
import os.path, os


def write_barcode(barcode: str) -> bool:
    """Escreve o código de barras no nosso txt (caso não esteja lá)

    Args:
        barcode (str): Código de barras

    Returns:
        bool: write_in_file
    """

    # Escreve o código de barras no txt se ele já não estiver lá
    dirpath = os.path.abspath("/ScrapperData")
    filepath = os.path.join(dirpath, "sysargs")

    # Cria o diretório se ele não existe
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)

    # Cria o arquivo se ele não existe
    if not os.path.exists(filepath):
        with open(filepath, "w+"):
            pass

    # Escreve no txt
    with open(filepath, "r+") as file:
        write_in_file = barcode not in file.read()
        if write_in_file:
            file.write(barcode + "\n")

        return write_in_file


def get_product_object_or_404(entity, barcode: str):
    try:
        target = entity.objects.get(pk=barcode)
        return target
    except entity.DoesNotExist:
        write_barcode(barcode)  # Se não estiver rodando da vm, comentar essa linha
        raise Http404


# Cria a view da lista completa de Safety (perdão pela não tradução)
class SafetyList(viewsets.ModelViewSet):
    queryset = Safety.objects.all()
    serializer_class = SafetySerializer
    filter_backends = (FiltroSafety,)

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "post":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        elif (
            self.action == "retrieve"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        elif self.action == "list" or self.action == "destroy":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        return [permission() for permission in permission_classes]


# Cria a view da lista completa de laudos
class ReportList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = (FiltroReport,)

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "post":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        elif (
            self.action == "retrieve"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        elif self.action == "list" or self.action == "destroy":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        return [permission() for permission in permission_classes]


# Cria a view da lista completa de marcas
class BrandList(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (FiltroBrand,)

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "post":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        elif (
            self.action == "retrieve"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        elif self.action == "list" or self.action == "destroy":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        return [permission() for permission in permission_classes]


# Cria a view da lista completa de produtos
class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (FiltroProduct,)

    def get_permissions(self):
        permission_classes = []
        if (
            self.request.method == "post"
            or self.action == "destroy"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            permission_classes = [
                IsAdminUser,
            ]
        elif self.action == "list" or self.action == "retrieve":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        return [permission() for permission in permission_classes]


# Cria a view da lista completa de analises
class ReviewList(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (FiltroReview,)

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "post":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        elif (
            self.action == "retrieve"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        elif self.action == "list" or self.action == "destroy":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]
        return [permission() for permission in permission_classes]


# View que dado um barCode, retorna um merge da do produto com as tabelas safety, brand e report
class ProductJoinedDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, entity, pk):
        return get_product_object_or_404(entity, pk)

    def get(self, request, barCode):

        product = self.get_object(Product, barCode)

        product_serialized = ProductSerializer(product, context={"request": request})
        brand = BrandSerializer(product.idBrand, context={"request": request})
        safety = SafetySerializer(product.idSafety, context={"request": request})

        test_dict = {**product_serialized.data, **brand.data, **safety.data}

        return Response(test_dict)


# Cria a view do detalhamento (GET, PUT, DELETE) de uma única safety a partir de sua idSafety
class SafetyDetail(viewsets.ModelViewSet):
    serializer_class = SafetySerializer

    def get_queryset(self):
        return Safety.objects.filter(book_id=self.kwargs["idSafety"])

    def get_permissions(self):
        permission_classes = []

        if self.action == "retrieve" or self.action == "list":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]

        elif (
            self.action == "destroy"
            or self.action == "update"
            or self.action == "partial_update"
            or self.request.method == "post"
        ):
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


# Cria a view do detalhamento (GET, PUT, DELETE) de uma única marca a partir de sua idBrand
class BrandDetail(viewsets.ModelViewSet):
    serializer_class = BrandSerializer

    def get_queryset(self):
        return Brand.objects.filter(book_id=self.kwargs["idBrand"])

    def get_permissions(self):
        permission_classes = []

        if self.action == "retrieve" or self.action == "list":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]

        elif (
            self.action == "destroy"
            or self.action == "update"
            or self.action == "partial_update"
            or self.request.method == "post"
        ):
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


# Cria a view do detalhamento (GET, PUT, DELETE) de um único laudo a partir de sua idReport
class ReportDetail(viewsets.ModelViewSet):
    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.filter(book_id=self.kwargs["idReport"])

    def get_permissions(self):
        permission_classes = []

        if self.action == "retrieve" or self.action == "list":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]

        elif (
            self.action == "destroy"
            or self.action == "update"
            or self.action == "partial_update"
            or self.request.method == "post"
        ):
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


# Cria a view do detalhamento (GET, PUT, DELETE) de um único produto a partir de sua barCode
class ProductDetail(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(book_id=self.kwargs["idProduct"])

    def get_permissions(self):
        permission_classes = []

        if self.action == "retrieve" or self.action == "list":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]

        elif (
            self.action == "destroy"
            or self.action == "update"
            or self.action == "partial_update"
            or self.request.method == "post"
        ):
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


# Cria a view do detalhamento (GET, PUT, DELETE) de uma única analise a partir de sua idReview
class ReviewDetail(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs["idReview"])

    def get_permissions(self):
        permission_classes = []

        if self.action == "retrieve" or self.action == "list":
            permission_classes = [
                IsLoggedInUserOrAdmin,
            ]

        elif (
            self.action == "destroy"
            or self.action == "update"
            or self.action == "partial_update"
            or self.request.method == "post"
        ):
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


# class FileView(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)

#     def getFile(self, request, path):
#         return Response(path)
