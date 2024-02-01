from rest_framework import serializers
from .models import Business, Campaign ,Product

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class ProductSerializer(serializers.ModelSerial):
    class Meta:
        model = Product
        fields = '__all__'