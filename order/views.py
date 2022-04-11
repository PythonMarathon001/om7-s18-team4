
from .models import Order
from .serializers import OrderDetail, OrderList
from rest_framework import generics


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetail

class OrderlistView(generics.ListAPIView):
    serializer_class = OrderList
    queryset = Order.objects.all()

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetail
    queryset = Order.objects.all()
