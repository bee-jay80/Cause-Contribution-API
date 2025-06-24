from rest_framework import serializers
from .models import Cause, Contribute

class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = ['id', 'title', 'description', 'image', 'image_url']
        read_only_fields = ['image_url']  # image_url is set automatically after upload

class ContributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribute
        fields = ['id', 'cause', 'name', 'email', 'amount', 'created_at']
        read_only_fields = ['created_at','cause']  # created_at is set automatically