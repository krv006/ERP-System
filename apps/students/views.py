from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny

from students.models import StudentJourney, Language
from students.serializers import StudentJourneyModelSerializer, StudentJourneyInJobModelSerializer, \
    StudentJourneyStatusUpdateModelSerializer, LanguageModelSerializer


@extend_schema(tags=['student'])
class StudentJourneyListCreateAPIView(ListCreateAPIView):
    queryset = StudentJourney.objects.all()
    serializer_class = StudentJourneyModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['student'])
class StudentJourneyInJobListAPIView(ListAPIView):
    queryset = StudentJourney.objects.all()
    serializer_class = StudentJourneyInJobModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['student'])
class StudentJourneyStatusUpdateAPIView(UpdateAPIView):
    queryset = StudentJourney.objects.all()
    serializer_class = StudentJourneyStatusUpdateModelSerializer
    permission_classes = AllowAny,  # faqat adminlarga ruxsat
    lookup_field = 'pk'  # default: 'pk', kerak bo‘lsa 'id' deb ham qo‘yish mumkin


@extend_schema(tags=['student'])
class LanguageListCreateAPIView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageModelSerializer
    permission_classes = AllowAny,

