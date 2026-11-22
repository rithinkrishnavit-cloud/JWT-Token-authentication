from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(["POST"])
def register(request):

    username = request.data.get("username")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return Response(
            {"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(username=username, password=password)

    return Response(
        {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
    )
