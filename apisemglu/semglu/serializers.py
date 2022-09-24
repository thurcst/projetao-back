from rest_framework import serializers
from .models import User, Safety, Report, Brand, Product
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'

class SafetySerializer(serializers.ModelSerializer):

    class Meta:

        model = Safety
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):

    class Meta:

        model = Report
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):

    class Meta:

        model = Brand
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

class ProductJoinedSerializer(serializers.ModelSerializer):
    brandName = serializers.SerializerMethodField()
    brandContact = serializers.SerializerMethodField()
    brandLogoPath = serializers.SerializerMethodField()

    def get_brandName(self, obj):
        return obj.idBrand.brandName

    def get_brandContact(self, obj):
        return obj.idBrand.contact

    def _get_picturePath(self, picture_url):
        #TODO: caminho da figura
        pass

    def get_brandLogoPath(self,obj):
        path = obj.idBrand.logoPath
        return self._get_picturePath(path)

    class Meta:
        model = Product
        fields = '__all__'
