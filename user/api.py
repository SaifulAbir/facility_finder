from rest_framework import serializers
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
import requests
from urllib.parse import quote
from user.models import User
from user.serializers import UserRegSerializer, CustomTokenObtainPairSerializer, UserProfileUpdateSerializer, \
    ChangeFavoriteFacilitySerializer, UserProfileSerializer


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

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.street_house_number and instance.city:
            user_address = f"{instance.street_house_number}, {instance.city}, {instance.state}"

            # Geocode the address using OpenCage API
            api_key = 'ce86b03caee641d08c94e2dc041a70d2'  # Replace with your OpenCage API key
            url = f"https://api.opencagedata.com/geocode/v1/json?q={quote(user_address)}&key={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data['results']:
                    lat = data['results'][0]['geometry']['lat']
                    lon = data['results'][0]['geometry']['lng']
                    instance.lat = lat
                    instance.long = lon
                    instance.save()
                else:
                    raise serializers.ValidationError("No data found for this address")
            else:
                raise serializers.ValidationError("Failed to fetch data from the geocoding service")
        else:
            raise serializers.ValidationError("Please update your address")
        return instance


class UserProfileAPIView(RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        user = User.objects.get(id=self.request.user.id)
        return user


class ChangeFavoriteFacilityAPIView(UpdateAPIView):
    serializer_class = ChangeFavoriteFacilitySerializer

    def get_object(self):
        return self.request.user


class DeleteAccountAPIView(APIView):

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()

        return Response({"message": "User deleted"})

