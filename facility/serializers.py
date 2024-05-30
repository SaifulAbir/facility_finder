from rest_framework import serializers
from facility.models import School, SocialWork, YouthCareer, Daycare


class SchoolListSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['id', 'object_id', 'category', 'lat', 'long']


class SocialWorkListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialWork
        fields = ['id', 'object_id', 'category', 'lat', 'long']


class YouthCareerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = YouthCareer
        fields = ['id', 'object_id', 'category', 'lat', 'long']


class DaycareListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Daycare
        fields = ['id', 'object_id', 'category', 'lat', 'long']