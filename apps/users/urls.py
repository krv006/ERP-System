from django.urls import path

from users.views import UserListAPIView, UserRegisterCreateView, LoginAPIView, UserRoleUpdateAPIView, \
    StudentJourneyListCreateAPIView, StudentJourneyInJobListAPIView

urlpatterns = [
    # todo USER
    path('user-list/', UserListAPIView.as_view(), name='user_list'),
    path('update-role/<int:pk>/', UserRoleUpdateAPIView.as_view(), name='user-update-role'),
    path('student-journey/', StudentJourneyListCreateAPIView.as_view(), name='student_journey_list'),
    path('student-journey-in-job/', StudentJourneyInJobListAPIView.as_view(), name='student_journey_in_job_list'),

    path('user-register/', UserRegisterCreateView.as_view(), name='register'),
    path('user-login/', LoginAPIView.as_view(), name='login'),
]
