from rest_framework import serializers
from .models import Course

class GetAllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'price','content',)


class CourseSerializer(serializers.Serializer):
    title1 = serializers.CharField(max_length=255)
    price1 = serializers.IntegerField()
    content1 = serializers.CharField(max_length=255)