from django.urls import path
from .views import StudentListView, ClassPeriodView, TeacherListView,CourseListView,StudentDetailView,ClassRoomListView,ClassRoomDetailView,CourseDetailView

urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("class_periods/", ClassPeriodView.as_view(), name="class_period_view"),
    path("classes/", ClassRoomListView.as_view(), name="classroom_list_view"),
    path("course/", CourseListView.as_view(), name="course_list_view"),
    path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
    path("students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),
    path("classes/<int:id>/", ClassRoomDetailView.as_view(), name="classroom_detail_view"),
    path("course/<int:id>/", CourseDetailView.as_view(), name="course_detail_view"),



]
