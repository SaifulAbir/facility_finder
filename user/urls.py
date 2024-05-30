from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from user.api import UserRegisterApi, CustomTokenObtainPairView, UserUpdateAPIView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register-user/', csrf_exempt(UserRegisterApi.as_view())),
    path('update-user/', UserUpdateAPIView.as_view()),
    path('user-profile/', UserUpdateAPIView.as_view()),
]