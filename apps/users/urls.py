from django.urls import path

from users.views import UserListAPIView, UserRegisterCreateView, LoginAPIView, UserRoleUpdateAPIView, \
    StudentJourneyListCreateAPIView, StudentJourneyInJobListAPIView, StudentJourneyStatusUpdateAPIView, \
    LanguageListCreateAPIView

urlpatterns = [
    # todo USER
    path('user-list/', UserListAPIView.as_view(), name='user_list'),
    path('update-role/<int:pk>/', UserRoleUpdateAPIView.as_view(), name='user-update-role'),
    path('student-journey/', StudentJourneyListCreateAPIView.as_view(), name='student-journey-list'),
    path('student-journey-in-job/', StudentJourneyInJobListAPIView.as_view(), name='student-journey-in-job-list'),
    path('update-status/<int:pk>/', StudentJourneyStatusUpdateAPIView.as_view(), name='student-journey-update-status'),
    path('language-journey/', LanguageListCreateAPIView.as_view(), name='language-list'),

    path('user-register/', UserRegisterCreateView.as_view(), name='register'),
    path('user-login/', LoginAPIView.as_view(), name='login'),
]
