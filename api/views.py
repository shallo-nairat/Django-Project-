
from django.shortcuts import render
from student.models import Student
from classperiod.models import ClassPeriod
from teacher.models import Teacher
from course.models import Course
from classroom.models import ClassRoom

from rest_framework import status

from .serializer import Student

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentSerializer
from .serializer import ClassPeriodSerializer
from .serializer import TeacherSerializer
from .serializer import CourseSerializer
from .serializer import ClassRoomSerializer




class ClassRoomListView(APIView):
    def get(self, request):
       classes = ClassRoom.objects.all()
       serializer = ClassRoomSerializer(classes,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        

class ClassRoomDetailView(APIView):
    def get(self, request, id):
        classes=ClassRoom.objects.get(id=id)
        serializer =ClassRoomSerializer (classes)
        return Response (serializer.data)   
     
    def put(self,request,id):
        classes=ClassRoom.objects.get(id=id)
        serializer =ClassRoomSerializer (classes)

        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id):
        classes =ClassRoom.objects.get(id=id)
        classes.delete()
        return Response (status=status.HTTP_202_ACCEPTED)    



class StudentListView(APIView):
    def get(self, request):
       students = Student.objects.all()
       serializer = StudentSerializer(students,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        

        
class StudentDetailView(APIView):
    def get(self, request, id):
        student=Student.objects.get(id=id)
        serializer =StudentSerializer (student)
        return Response (serializer.data)   
     
    def put(self,request,id):
        student=Student.objects.get(id=id)
        serializer =StudentSerializer (student)

        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id):
        student =Student.objects.get(id=id)
        student.delete()
        return Response (status=status.HTTP_202_ACCEPTED)    


class ClassPeriodView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class  ClassPeriodDetailView(APIView):
    def get(self, request, id):
        class_periods=ClassPeriod.objects.get(id=id)
        serializer =ClassPeriodSerializer (class_periods)
        return Response (serializer.data)   
     
    def put(self,request,id):
        class_periods=ClassPeriod.objects.get(id=id)
        serializer =ClassPeriodSerializer(class_periods)

        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id):
        class_periods =ClassPeriod.objects.get(id=id)
        class_periods.delete()
        return Response (status=status.HTTP_202_ACCEPTED)    


        
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        



class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher=Teacher.objects.get(id=id)
        serializer =TeacherSerializer (teacher)
        return Response (serializer.data)   
     
    def put(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher)

        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id):
        teacher =Teacher.objects.get(id=id)
        teacher.delete()
        return Response (status=status.HTTP_202_ACCEPTED)    





class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)



class CourseDetailView(APIView):
    def get(self, request, id):
        course=Course.objects.get(id=id)
        serializer = CourseSerializer(course, many=True)
        serializer =CourseSerializer (course)
        return Response (serializer.data)   



    def put(self,request,id):
        course=Course.objects.get(id=id)
        serializer =CourseSerializer(course)

        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id):
        course =Course.objects.get(id=id)
        course.delete()
        return Response (status=status.HTTP_202_ACCEPTED) 



