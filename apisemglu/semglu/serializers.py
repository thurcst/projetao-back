from rest_framework import serializers
from .models import User, Safety, Report, Brand, Product

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
    

