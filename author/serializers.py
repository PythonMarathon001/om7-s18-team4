from rest_framework import serializers
from .models import Author



class AuthorList(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorDetail(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

