from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from user.api import UserRegisterAPIView, CustomTokenObtainPairView, UserUpdateAPIView, ChangeFavoriteFacilityAPIView, \
    UserProfileAPIView, DeleteAccountAPIView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register-user/', csrf_exempt(UserRegisterAPIView.as_view())),
    path('update-user/', UserUpdateAPIView.as_view()),
    path('user-profile/', UserProfileAPIView.as_view()),
    path('change-favorite-facility/', ChangeFavoriteFacilityAPIView.as_view()),
    path('delete-user/', DeleteAccountAPIView.as_view()),
]