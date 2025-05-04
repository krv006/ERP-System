from django.urls import path

from users.views import UserListAPIView, UserRegisterCreateView, LoginAPIView, UserRoleUpdateAPIView, \
    StudentJourneyListCreateAPIView

urlpatterns = [
    # todo USER
    path('users/', UserListAPIView.as_view(), name='user_list'),
    path('update-role/<int:pk>/', UserRoleUpdateAPIView.as_view(), name='user-update-role'),
    path('student-journey/', StudentJourneyListCreateAPIView.as_view(), name='student_journey_list'),

    path('register/', UserRegisterCreateView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
