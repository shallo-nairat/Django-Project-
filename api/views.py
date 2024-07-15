from django.shortcuts import render

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