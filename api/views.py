import json
from typing import Dict

from django.http import HttpRequest, JsonResponse, HttpResponse
from django.views import View

from oauth.models import Token
from serializers.serializers import GradeSerializer, LoginSerializer
from main.models import Teacher, Course, Project, Grade
from oauth.wrappers import teacher_api_authenticated
from serializers.wrappers import validate_data


class LoginApiView(View):

    @validate_data(LoginSerializer)
    def post(self, request: HttpRequest, data: Dict) -> JsonResponse:
        """
        Login the teacher and generate a 'oauth' token
        :param request:
        :param data:
        :return:
        """

        teacher = Teacher.login(**data)
        token = Token()
        token.teacher = teacher
        token.save()

        return JsonResponse(status=200, data={
            "token": token.token
        })


class CourseApiView(View):

    @teacher_api_authenticated
    def get(self, request: HttpRequest, teacher: Teacher) -> JsonResponse:
        """
        Get the courses from the assigned teacher
        :param request:
        :param teacher:
        :return:
        """
        courses = Course.objects.filter(teacher=teacher).values()
        print('\033[92m{}\033[0m'.format(courses))
        return JsonResponse(status=200, data={'courses': list(courses)})


class ProjectApiView(View):

    @teacher_api_authenticated
    def get(self, request: HttpRequest, course_id: str, teacher: Teacher) -> JsonResponse:
        """
        Get the courses from the assigned teacher
        :param request:
        :param teacher:
        :return:
        """
        projects = Project.objects.filter(course_id=course_id).values()
        return JsonResponse(status=200, data={'projects': list(projects)})


class GradeApiView(View):

    def format_grade(self, grade: Grade):
        """
        Format the grade object to show the studen and the grade the student got
        :param grade:
        :return:
        """
        return {
            "id": grade.student.id,
            "name": grade.student.name,
            "grade": grade.score
        }

    @teacher_api_authenticated
    def get(self, request: HttpRequest, project_id: str,  teacher: Teacher) -> JsonResponse:
        """
        Get the grades the studens got for a project
        :param request:
        :param teacher:
        :return:
        """
        project = Project.objects.get(id=project_id)
        grades = project.grade_set.select_related('student').all()

        return JsonResponse(status=200, data={
            'project_id': project_id,
            'project_name': project.name,
            'student_grades': [self.format_grade(grade) for grade in grades]
        })

    @teacher_api_authenticated
    @validate_data(serializer=GradeSerializer)
    def post(self, request: HttpRequest, project_id: str,
             teacher: Teacher, data: Dict) -> JsonResponse:
        """
        Update the grade from the student for the given project
        :param request:
        :param project_id:
        :param teacher:
        :param data:
        :return:
        """
        grade = Grade.objects.get(
            project_id=project_id, student_id=data.get('student_id'))
        grade.score = data.get('score')
        grade.save()

        return JsonResponse(status=201, data={})
