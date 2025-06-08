from django.urls import path

from users.views import UserListAPIView, UserRegisterCreateView, LoginAPIView, UserRoleUpdateAPIView, \
    UserDetailListAPIView, VerifyCodeApiView

urlpatterns = [
    # todo USER
    path('user-list/', UserListAPIView.as_view(), name='user_list'),
    path('user-detail/', UserDetailListAPIView.as_view(), name='user_deatil'),
    path('update-role/<int:pk>/', UserRoleUpdateAPIView.as_view(), name='user-update-role'),

    # todo Login-Register
    path('user-register/', UserRegisterCreateView.as_view(), name='register'),
    path('verify-code', VerifyCodeApiView.as_view(), name='verify_code'),
    path('user-login/', LoginAPIView.as_view(), name='login'),
]
