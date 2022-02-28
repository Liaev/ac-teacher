import uuid
from django.db import models


class Teacher(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255,) # I know this is plain text password storage. But it only for demo purpose so fight me about it ;)

    @classmethod
    def login(cls, username: str, password: str) -> "Teacher":
        """
        Get the teacher based on login credentials
        :param username:
        :param password:
        :return:
        """
        return cls.objects.get(username=username, password=password)


class Student(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)


class Course(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(Student)


class Project(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(Student, through='Grade')


class Grade(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    score = models.DecimalField(max_digits=4, decimal_places=2, null=True)
