from rest_framework import serializers
from .models import Book



class BookList(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookDetail(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'