from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User
from user.serializers import UserRegSerializer, CustomTokenObtainPairSerializer, UserProfileUpdateSerializer, \
    ChangeFavoriteFacilitySerializer


class UserRegisterApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class UserUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfileUpdateSerializer

    def get_object(self):
        user = User.objects.get(id=self.request.user.id)
        return user


class ChangeFavoriteFacilityAPIView(UpdateAPIView):
    serializer_class = ChangeFavoriteFacilitySerializer

    def get_object(self):
        return self.request.user

