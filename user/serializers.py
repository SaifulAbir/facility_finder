from rest_framework import serializers, status
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from facility.models import Daycare, School, SocialWork, YouthCareer
from facility.serializers import DaycareListSerializer, SchoolListSerializer, SocialWorkListSerializer, \
    YouthCareerListSerializer
from user.models import User


class UserRegSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        refresh = self.get_token(self.user)
        data.update({'user_id': self.user.id,
                     'lifetime': int(refresh.access_token.lifetime.total_seconds())})
        return data


class UserProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'street_house_number', 'city', 'state', 'lat', 'long']


class UserProfileSerializer(serializers.ModelSerializer):
    favorite_facility = serializers.SerializerMethodField('favorite_facility_data')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'favorite_facility', 'street_house_number', 'city', 'state',
                  'is_active', 'lat', 'long']

    def favorite_facility_data(self, obj):
        if obj.favorite_facility_category == "Kindertageseinrichtungen":
            favorite_facility_obj = Daycare.objects.get(id=obj.favorite_facility_id)
            return DaycareListSerializer(favorite_facility_obj).data
        elif obj.favorite_facility_category == "Schulen":
            favorite_facility_obj = School.objects.get(id=obj.favorite_facility_id)
            return SchoolListSerializer(favorite_facility_obj).data
        elif obj.favorite_facility_category == "Schulsozialarbeit":
            favorite_facility_obj = SocialWork.objects.get(id=obj.favorite_facility_id)
            return SocialWorkListSerializer(favorite_facility_obj).data
        elif obj.favorite_facility_category == "Jugendberufshilfen":
            favorite_facility_obj = YouthCareer.objects.get(id=obj.favorite_facility_id)
            return YouthCareerListSerializer(favorite_facility_obj).data


class ChangeFavoriteFacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('favorite_facility_id', 'favorite_facility_category')