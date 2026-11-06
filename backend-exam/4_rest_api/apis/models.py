from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=10)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"


class Classroom(models.Model):
    grade_level = models.IntegerField()
    classroom_number = models.CharField(max_length=10)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="classrooms"
    )

    def __str__(self):
        return f"ชั้น {self.grade_level} ห้อง {self.classroom_number}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(
        Classroom, related_name="teachers", blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.SET_NULL, related_name="students", null=True, blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
