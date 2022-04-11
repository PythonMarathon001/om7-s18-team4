from django.urls import path
from .views import BookCreateView, BooklistView, BookDetailView
from . import views

urlpatterns = [
    path('book/create', BookCreateView.as_view()),
    path('all/', BooklistView.as_view()),
    path('book/detail/<int:pk>/', BookDetailView.as_view()),
]