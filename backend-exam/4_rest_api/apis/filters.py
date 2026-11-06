from django_filters import FilterSet, filters
from .models import School, Classroom, Teacher, Student


class SchoolFilter(FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model = School
        fields = ["name", "abbreviation"]


class ClassroomFilter(FilterSet):
    school = filters.NumberFilter(field_name="school__id")
    grade_level = filters.NumberFilter(field_name="grade_level")

    class Meta:
        model = Classroom
        fields = ["school", "grade_level"]


class TeacherFilter(FilterSet):
    school = filters.NumberFilter(field_name="classrooms__school__id")
    classroom = filters.NumberFilter(field_name="classrooms__id")
    firstname = filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    lastname = filters.CharFilter(field_name="last_name", lookup_expr="icontains")
    gender = filters.CharFilter(field_name="gender")

    class Meta:
        model = Teacher
        fields = ["school", "classroom", "firstname", "lastname", "gender"]


class StudentFilter(FilterSet):
    school = filters.NumberFilter(field_name="classroom__school__id")
    classroom = filters.NumberFilter(field_name="classroom__id")
    firstname = filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    lastname = filters.CharFilter(field_name="last_name", lookup_expr="icontains")
    gender = filters.CharFilter(field_name="gender")

    class Meta:
        model = Student
        fields = ["school", "classroom", "firstname", "lastname", "gender"]



