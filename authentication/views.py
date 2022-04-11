from .models import CustomUser
from .serializers import UserDetail, UserList
from rest_framework import generics


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetail

class UserlistView(generics.ListAPIView):
    serializer_class = UserList
    queryset = CustomUser.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetail
    queryset = CustomUser.objects.all()