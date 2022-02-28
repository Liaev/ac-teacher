from django.contrib import admin

# Register your models here.
from main.models import Teacher, Course, Student, Grade


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass
