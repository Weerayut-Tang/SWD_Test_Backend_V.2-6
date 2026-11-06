from rest_framework import serializers
from .models import School, Classroom, Teacher, Student


class SchoolSerializer(serializers.ModelSerializer):
    class_count = serializers.IntegerField(read_only=True)
    teacher_count = serializers.IntegerField(read_only=True)
    student_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = School
        fields = ["id", "name", "abbreviation", "address", "class_count", "teacher_count", "student_count"]

    def create(self, validated_data):
        return School.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.abbreviation = validated_data.get("abbreviation", instance.abbreviation)
        instance.address = validated_data.get("address", instance.address)
        instance.save()
        return instance


class ClassroomSerializer(serializers.ModelSerializer):
    teacher_count = serializers.IntegerField(read_only=True)
    student_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Classroom
        fields = ["id", "grade_level", "classroom_number", "school", "teacher_count", "student_count"]

    def create(self, validated_data):
        return Classroom.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.grade_level = validated_data.get("grade_level", instance.grade_level)
        instance.classroom_number = validated_data.get("classroom_number", instance.classroom_number)
        instance.school = validated_data.get("school", instance.school)
        instance.save()
        return instance


class TeacherSerializer(serializers.ModelSerializer):
    classroom_names = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ["id", "first_name", "last_name", "gender", "classroom_names"]

    def get_classroom_names(self, obj):
        return [str(c) for c in obj.classrooms.all()]

    def create(self, validated_data):
        classroom_data = validated_data.pop("classrooms", [])
        teacher = Teacher.objects.create(**validated_data)
        if classroom_data:
            for cls in classroom_data:
                teacher.classrooms.add(cls)
        return teacher

    def update(self, instance, validated_data):
        classroom_data = validated_data.pop("classrooms", None)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.save()
        if classroom_data is not None:
            instance.classrooms.set(classroom_data)
        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "gender", "classroom"]

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.classroom = validated_data.get("classroom", instance.classroom)
        instance.save()
        return instance
