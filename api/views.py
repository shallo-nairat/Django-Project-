
from django.shortcuts import render
from student.models import Student
from ClassPeriod.models import ClassPeriod
from teacher.models import Teacher
from course.models import Course

from .serializer import Student

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentSerializer
from .serializer import ClassPeriodSerializer
from .serializer import TeacherSerializer
from .serializer import CourseSerializer



class StudentListView(APIView):
    def get(self, request):
       students = Student.objects.all()
       serializer = StudentSerializer(students,many=True)
       return Response(serializer.data)
    
class ClassPeriodView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)



class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)



class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)






# from django.shortcuts import render

# Create your views here.

# from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from student.models import Student
# from serializer import StudentSerializer



# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = "__all__"


# class StudentListView(APIView):
#     def get(self, request):
#     students= Student.objects.all()
#     serializers = StudentSerializer(students,many=True)
#     return Response(serializers.data)