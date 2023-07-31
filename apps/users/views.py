from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from users.models import Users
from users.serializer import UserCreateSerializer


class RegistrationView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserCreateSerializer
