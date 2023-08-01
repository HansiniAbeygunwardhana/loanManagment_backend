from rest_framework import serializers
from .models import analytics


class AanalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = analytics
        fields = '__all__'