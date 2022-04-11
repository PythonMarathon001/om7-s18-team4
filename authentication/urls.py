from django.urls import path

from .views import UserCreateView, UserDetailView, UserlistView

urlpatterns = [
    path('user/create', UserCreateView.as_view()),
    path('all/', UserlistView.as_view()),
    path('user/detail/<int:pk>/', UserDetailView.as_view()),
]