from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import GetAllCourseSerializer, CourseSerializer
import json

class GetAllCoursesAPIView(APIView):

    def get(self, request):
        list_courses = Course.objects.all()
        mydata = GetAllCourseSerializer(list_courses, many =True)
        return Response(data=mydata.data, status = status.HTTP_200_OK)

    def post(self, request):
        mydata = data=request.data

        with open("D:/file.json", "w+") as f:
            json.dump(mydata, f)


        return Response(data=mydata, status=status.HTTP_200_OK)