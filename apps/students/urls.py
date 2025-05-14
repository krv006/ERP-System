from django.urls import path

from students.views import StudentJourneyListCreateAPIView, StudentJourneyInJobListAPIView, \
    StudentJourneyStatusUpdateAPIView, LanguageListCreateAPIView, StudentListCreateAPIView

urlpatterns = [
    # todo Student
    path('student-list/', StudentListCreateAPIView.as_view(), name='student-list'),
    path('student-journey/', StudentJourneyListCreateAPIView.as_view(), name='student-journey-list'),
    path('student-journey-in-job/', StudentJourneyInJobListAPIView.as_view(), name='student-journey-in-job-list'),
    path('update-status/<int:pk>/', StudentJourneyStatusUpdateAPIView.as_view(), name='student-journey-update-status'),
    path('language-journey/', LanguageListCreateAPIView.as_view(), name='language-list')

]
