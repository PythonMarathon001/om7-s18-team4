from rest_framework import serializers
from .models import CustomUser



class UserList(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserDetail(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'