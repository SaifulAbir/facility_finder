from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User
from user.serializers import UserRegSerializer, CustomTokenObtainPairSerializer, UserProfileUpdateSerializer, \
    ChangeFavoriteFacilitySerializer, ChangeHomeAddressSerializer, UserProfileSerializer


class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfileUpdateSerializer

    def get_object(self):
        user = User.objects.get(id=self.request.user.id)
        return user


class UserProfileAPIView(RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        user = User.objects.get(id=self.request.user.id)
        return user


class ChangeFavoriteFacilityAPIView(UpdateAPIView):
    serializer_class = ChangeFavoriteFacilitySerializer

    def get_object(self):
        return self.request.user


class ChangeHomeAddressAPIView(UpdateAPIView):
    serializer_class = ChangeHomeAddressSerializer

    def get_object(self):
        return self.request.user


class DeleteAccountAPIView(APIView):

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()

        return Response({"message": "User deleted"})

