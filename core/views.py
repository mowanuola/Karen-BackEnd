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
from core.dci import calculateDCI


class RegisterView(APIView):
    def post(self, request):
        form = RegisterForm(request.data or None)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            email = form.cleaned_data['email'].lower()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            sex = form.cleaned_data['sex']
            birth_date = form.cleaned_data['birth_date']
            user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name, birth_date=birth_date, sex=sex)
            user.set_password(form.cleaned_data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response(data={'token': token.key, 'message': "User successfully registered"}, status=status.HTTP_201_CREATED)
        return Response(data=form.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        return Response(data={'token': token.key})


class UserView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class CalculateBMIView(APIView):
    permission_classes = (IsAuthenticated, )

    def put(self, request):
        form = CalculateBMIForm(request.data or None)
        if form.is_valid():
            user = request.user
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            user.height = int(height)
            user.weight = int(weight)
            user.save()
            serializer = UserSerializer(user)
            return Response(data={'message': "Sucess", 'user': serializer.data})
        return Response(data=form.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CalculateDCIView(APIView):
    permission_classes = (IsAuthenticated, )

    def put(self, request):
        form = CalculateDCIForm(request.data or None)
        if form.is_valid():
            user = request.user
            useractivity = form.cleaned_data['useractivity']
            height  = user.height
            weight  = user.weight
            age  = user.age
            sex  = user.sex
            dci = calculateDCI(height,weight,sex,age,useractivity)
            user.dci = dci
            user.save()
            serializer = UserSerializer(user)
            return Response(data={'message': "Sucess", 'user': serializer.data})
        return Response(data=form.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
