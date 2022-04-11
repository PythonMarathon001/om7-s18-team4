from django.urls import path
from .views import AuthorCreateView, AuthorlistView, AuthorDetailView
from . import views

urlpatterns = [
    path('author/create', AuthorCreateView.as_view()),
    path('all/', AuthorlistView.as_view()),
    path('author/detail/<int:pk>/', AuthorDetailView.as_view()),
]