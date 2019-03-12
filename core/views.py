from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from core.models import *
from core.serializers import *
from django.db.models import Q
from random import shuffle
from core.forms import *


class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class RegisterView(APIView):
    def post(self, request):
        form = RegisterForm(request.data or None)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            email = form.cleaned_data['email'].lower()
            user = User(username=username, email=email)
            user.set_password(form.cleaned_data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response(data={'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(data=form.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})