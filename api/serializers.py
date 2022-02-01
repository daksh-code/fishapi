from . models import FishDetail
from rest_framework import serializers
class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishDetail
        fields = '__all__'