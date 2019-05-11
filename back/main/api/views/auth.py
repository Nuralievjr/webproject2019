from django.contrib.auth.models import User
from api.serializer import UserSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
