from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, ProfileView, UserListView
 
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='user-list'),
]
 
