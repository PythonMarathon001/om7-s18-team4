from django.urls import path
from .views import OrderCreateView, OrderlistView, OrderDetailView
from . import views

urlpatterns = [
    path('order/create', OrderCreateView.as_view()),
    path('all/', OrderlistView.as_view()),
    path('order/detail/<int:pk>/', OrderDetailView.as_view()),
]
