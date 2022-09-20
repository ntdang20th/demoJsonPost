from django.urls import path
from Course.views import GetAllCoursesAPIView

urlpatterns = [
    path('all/', GetAllCoursesAPIView.as_view(), name='getall'),
]
