from rest_framework import serializers
from .models import User
import django.contrib.auth.password_validation
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'username']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate_username(self, username):
        if len(username) < 5:
            raise serializers.ValidationError("The username must contain at least 5 characters")
        return username

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("The password must contain at least 8 characters")
        if not re.findall('\d', password):
            raise serializers.ValidationError("The password must contain at least 1 digit, 0-9.")
        if not re.findall('[A-Z]', password):
            raise serializers.ValidationError("The password must contain at least 1 uppercase letter, A-Z.")
        if not re.findall('[a-z]', password):
            raise serializers.ValidationError("The password must contain at least 1 lowercase letter, a-z.")
        return password

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 