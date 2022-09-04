from urllib import response
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User, Safety, Report, Brand, Product
from .serializers import UserSerializer, SafetySerializer, ReportSerializer, BrandSerializer, ProductSerializer

# Create your views here.
class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_pkey(request, idUser):
        try:
            User.objects.get(pk=idUser)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SafetyList(generics.ListCreateAPIView):

    queryset = Safety.objects.all()
    serializer_class = SafetySerializer


class SafetyDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_pkey(request, idSafety):
        try:
            Safety.objects.get(pk=idSafety)
        except Safety.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    queryset = Safety.objects.all()
    serializer_class = SafetySerializer


class ReportList(generics.ListCreateAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_pkey(request, idReport):
        try:
            Report.objects.get(pk=idReport)
        except Report.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class BrandList(generics.ListCreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_pkey(request, idBrand):
        try:
            Brand.objects.get(pk=idBrand)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    queryset = Safety.objects.all()
    serializer_class = BrandSerializer


class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_pkey(request, idProduct):
        try:
            Product.objects.get(pk=idProduct)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    queryset = Safety.objects.all()
    serializer_class = ProductSerializer
