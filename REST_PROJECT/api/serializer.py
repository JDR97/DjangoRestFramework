from rest_framework import serializers
from .models import User


##Convert or Transform the model to JSON for API
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'