from rest_framework import serializers
from facility.models import School, SocialWork, YouthCareer, Daycare


class SchoolListSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['id', 'object_id', 'typ', 'art', 'standorttyp', 'category', 'bezeichnung', 'bezeichnungzusatz',
                  'kurzbezeichnung', 'strasse', 'plz', 'ort', 'telefon', 'fax', 'email', 'profile', 'lat', 'long',
                  'sprachen', 'www', 'traeger', 'traegertyp', 'bezugnr', 'gebietsartnummer', 'snummer', 'nummer',
                  'global_id']


class SocialWorkListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialWork
        fields = '__all__'


class YouthCareerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = YouthCareer
        fields = '__all__'


class DaycareListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Daycare
        fields = ['id', 'object_id', 'category', 'lat', 'long', 'traeger', 'bezeichnung', 'kurzbezeichnung',
                  'strasse', 'strschl', 'hausbez', 'plz', 'ort', 'hort', 'kita', 'url', 'telefon', 'fax', 'email',
                  'barrierefrei', 'integrativ']