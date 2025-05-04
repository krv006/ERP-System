from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User, StudentJourney
from users.serializers import RegisterUserModelSerializer, LoginUserModelSerializer, UserModelSerializer, \
    UserRoleUpdateModelSerializer, StudentJourneyModelSerializer, StudentJourneyInJobModelSerializer


@extend_schema(tags=['user'])
class UserRegisterCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['user'])
class LoginAPIView(GenericAPIView):
    serializer_class = LoginUserModelSerializer
    permission_classes = AllowAny,
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)


@extend_schema(tags=['user'])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = AllowAny,
    authentication_classes = ()


@extend_schema(tags=['user'])
class UserRoleUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRoleUpdateModelSerializer
    permission_classes = AllowAny,  # faqat adminlarga ruxsat
    lookup_field = 'pk'  # default: 'pk', kerak bo‘lsa 'id' deb ham qo‘yish mumkin


@extend_schema(tags=['user'])
class StudentJourneyListCreateAPIView(ListCreateAPIView):
    queryset = StudentJourney.objects.all()
    serializer_class = StudentJourneyModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['user'])
class StudentJourneyInJobListAPIView(ListAPIView):
    queryset = StudentJourney.objects.all()
    serializer_class = StudentJourneyInJobModelSerializer
    permission_classes = AllowAny,
