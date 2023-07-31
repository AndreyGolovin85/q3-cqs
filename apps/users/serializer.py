from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from users.models import Users


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = "__all__"

    def create(self, request):
        password = make_password(request["password"])
        user = Users.objects.create(**request | {"password": password})

        return user
