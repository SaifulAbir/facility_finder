from rest_framework.response import Response
from rest_framework.views import APIView
from facility.models import School, SocialWork, YouthCareer, Daycare
from facility.serializers import SchoolListSerializer, YouthCareerListSerializer, DaycareListSerializer


class FeatureListAPIView(APIView):

    def get(self, request):
        schools = School.objects.all()
        social_works = SocialWork.objects.all()
        youth_careers = YouthCareer.objects.all()
        daycares = Daycare.objects.all()
        school_serializer = SchoolListSerializer(schools, many=True)
        social_work_serializer = SchoolListSerializer(social_works, many=True)
        youth_career_serializer = YouthCareerListSerializer(youth_careers, many=True)
        daycare_serializer = DaycareListSerializer(daycares, many=True)
        return Response({"school_list": school_serializer.data, "social_work_list": social_work_serializer.data,
                         "youth_career_list": youth_career_serializer.data, "daycare_list": daycare_serializer.data})
