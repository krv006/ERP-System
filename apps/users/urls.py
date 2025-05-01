from django.urls import path

from users.views import UserListAPIView, UserRegisterCreateView, LoginAPIView

urlpatterns = [
    path('user/', UserListAPIView.as_view(), name='user_list'),
    path('register/', UserRegisterCreateView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
