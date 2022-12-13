from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import *


class LogoutJWT(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SignUp(APIView):
    def post(self, request):
        username = request.data['username']
        pass1 = request.data['password1']
        pass2 = request.data['password2']
        email = request.data['email']
        users = CustomUser.objects.filter(username=username)
        if users.exists():
            return Response(status=status.HTTP_409_CONFLICT)
        if pass2 != pass1:
            return Response({'message': 'Entered passwords are not identical'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            CustomUser.objects.create_user(username=username, password=pass1, email=email)
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)