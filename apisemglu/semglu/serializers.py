from rest_framework import serializers
from .models import User, Safety, Report, Brand, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = "__all__"


class SafetySerializer(serializers.ModelSerializer):
    class Meta:

        model = Safety
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):

    filePath = serializers.SerializerMethodField()

    class Meta:

        model = Report
        fields = "__all__"

    def get_filePath(self, obj):
        request = self.context.get("request")
        filePath_temp = obj.filePath.url
        return request.build_absolute_uri(filePath_temp)


class BrandSerializer(serializers.ModelSerializer):

    logoPath = serializers.SerializerMethodField()

    class Meta:

        model = Brand
        fields = "__all__"

    def get_logoPath(self, obj):
        request = self.context.get("request")
        logoPath_temp = obj.logoPath.url
        return request.build_absolute_uri(logoPath_temp)


class ProductSerializer(serializers.ModelSerializer):

    picturePath = serializers.SerializerMethodField()

    class Meta:

        model = Product
        fields = "__all__"

    def get_picturePath(self, obj):
        request = self.context.get("request")
        picturePath_temp = obj.picturePath.url
        return request.build_absolute_uri(picturePath_temp)


class ProductJoinedSerializer(serializers.ModelSerializer):
    brandName = serializers.SerializerMethodField()
    brandContact = serializers.SerializerMethodField()
    brandLogoPath = serializers.SerializerMethodField()

    def get_brandName(self, obj):
        return obj.idBrand.brandName

    def get_brandContact(self, obj):
        return obj.idBrand.contact

    def _get_picturePath(self, picture_url):
        # TODO: caminho da figura
        pass

    def get_brandLogoPath(self, obj):
        path = obj.idBrand.logoPath
        return self._get_picturePath(path)

    class Meta:
        model = Product
        fields = "__all__"
