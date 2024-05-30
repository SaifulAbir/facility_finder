from django.urls import path
from facility.api import FeatureListAPIView


urlpatterns = [
    path('features/', FeatureListAPIView.as_view(), name='feature_list'),
]