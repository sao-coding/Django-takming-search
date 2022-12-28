from django.shortcuts import render

from django.contrib import auth
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.

@api_view(["GET"])
def api(request):
    return Response({"message": "Hello, World!"})

@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = auth.authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"status": "success", "token": token.key}, status=200)
    else:
        return Response({"status": "fail"}, status=401)
