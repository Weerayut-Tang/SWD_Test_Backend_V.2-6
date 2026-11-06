from rest_framework import viewsets
from .models import School, Classroom, Teacher, Student
from .serializers import SchoolSerializer, ClassroomSerializer, TeacherSerializer, StudentSerializer
from .filters import SchoolFilter, ClassroomFilter, TeacherFilter, StudentFilter


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_class = SchoolFilter


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_class = ClassroomFilter


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_class = TeacherFilter


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_class = StudentFilter