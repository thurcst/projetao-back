from itertools import product
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
