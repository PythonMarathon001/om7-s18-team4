from django.shortcuts import render, redirect
from .forms import AuthorForm
from .models import Author
from .serializers import AuthorDetail, AuthorList
from rest_framework import generics


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorDetail

class AuthorlistView(generics.ListAPIView):
    serializer_class = AuthorList
    queryset = Author.objects.all()

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorDetail
    queryset = Author.objects.all()




