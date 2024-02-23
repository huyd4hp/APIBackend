from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","username",'password',"first_name","last_name","is_staff","is_active","date_joined","email","role","is_superuser","last_login"]
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user 