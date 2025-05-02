from django.urls import path

from users.views import UserListAPIView, UserRegisterCreateView, LoginAPIView, UserRoleUpdateAPIView

urlpatterns = [
    path('user/', UserListAPIView.as_view(), name='user_list'),
    path('update-role/<int:pk>/', UserRoleUpdateAPIView.as_view(), name='user-update-role'),
    path('register/', UserRegisterCreateView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
