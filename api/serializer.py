

from rest_framework import serializers
from classperiod.models import ClassPeriod

from student.models import Student
from course.models  import Course
from teacher.models import Teacher
from classroom.models import ClassRoom

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"

    # def get_age(self, object):
    #     if object.date_of_birth:
    #         today = datetime.now()
    #     if isinstance(object.date_of_birth, date) and not isinstance(object.date_of_birth, datetime):
    #         date_of_birth = datetime.combine(object.date_of_birth, datetime.min.time())
    #     else:
    #         date_of_birth = object.date_of_birth
        
    #     age = today - date_of_birth
    #     return age.days // 365  
    
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'age']

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'
class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ['id', 'name', 'start_time', 'end_time']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name','teacher']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"
    
    class Meta:
        model = Teacher
        fields = ['id', 'full_name','email']
        
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'



# class MinimalStudentSerializer(serializers.ModelSerializer):
#     full_name=serializer.SerializerMethodField
#     def get_full_name(self,object):
#         return f"{object.first_name}{object.last_name}"
    
#     class Meta:
#         model = Student
#         fields = ["id","first_name","code"]