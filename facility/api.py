from rest_framework.response import Response
from rest_framework.views import APIView
from facility.models import School, SocialWork, YouthCareer, Daycare
from facility.serializers import SchoolListSerializer, YouthCareerListSerializer, DaycareListSerializer


class FeatureListAPIView(APIView):

    def get(self, request):
        feature_dict = {"school_list": None, "social_work_list": None, "youth_career_list": None, "daycare_list": None}
        category_list = request.GET.getlist("category")

        for category in category_list:
            if category == "Schulen":
                schools = School.objects.all()
                school_serializer = SchoolListSerializer(schools, many=True)
                feature_dict["school_list"] = school_serializer.data

            if category == "Kindertageseinrichtungen":
                daycares = Daycare.objects.all()
                daycare_serializer = DaycareListSerializer(daycares, many=True)
                feature_dict["daycare_list"] = daycare_serializer.data

            if category == "Schulsozialarbeit":
                social_works = SocialWork.objects.all()
                social_work_serializer = SchoolListSerializer(social_works, many=True)
                feature_dict["social_work_list"] = social_work_serializer.data

            if category == "Jugendberufshilfen":
                youth_careers = YouthCareer.objects.all()
                youth_career_serializer = YouthCareerListSerializer(youth_careers, many=True)
                feature_dict["youth_career_list"] = youth_career_serializer.data

        return Response(feature_dict)
