from rest_framework import serializers
from .models import Review, User, Safety, Report, Brand, Product, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = "__all__"


class SafetySerializer(serializers.ModelSerializer):
    class Meta:

        model = Safety
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:

        model = Report
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:

        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        model = Product
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:

        model = Review
        fields = "__all__"
