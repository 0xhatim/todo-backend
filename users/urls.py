from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView, ProfileView,
    ProfilePictureView, ChangePasswordView, DeleteAccountView
)

app_name = 'users'

urlpatterns = [
    # Authentication endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Profile management endpoints
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/picture/', ProfilePictureView.as_view(), name='profile-picture'),
    path('profile/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('profile/delete/', DeleteAccountView.as_view(), name='delete-account'),
] 