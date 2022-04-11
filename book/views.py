
from .models import Book
from .serializers import BookDetail, BookList
from rest_framework import generics


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetail

class BooklistView(generics.ListAPIView):
    serializer_class = BookList
    queryset = Book.objects.all()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetail
    queryset = Book.objects.all()
