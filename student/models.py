from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    immediate_contact = models.CharField(max_length=100)
    enrollment_date = models.DateField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    bio = models.TextField()
    courses = models.ManyToManyField('course.Course', related_name='student')
    classes = models.ManyToManyField('class.Class', related_name='student')
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"