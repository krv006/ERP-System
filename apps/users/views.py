from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from users.models import User
from users.serializers import UserModelSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer