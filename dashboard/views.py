from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from dashboard.autentication import teacher_authenticate
from dashboard.forms import LoginForm, GradeForm
from main.models import Teacher, Course, Project, Grade


class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def login(self):
        pass

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Get the login form
        :param request:
        :return:
        """
        context = {'form': self.form_class()}
        return render(request, self.template_name, context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Login the teacher
        create a fake login that just creates a get parameter with the teacher id in it
        for demo purpose
        :param request:
        :return:
        """
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, context={"form": form})

        try:
            teacher = Teacher.objects.get(username=form.cleaned_data.get("username"),
                                          password=form.cleaned_data.get('password'))
        except Teacher.DoesNotExist:
            return render(request, self.template_name, context={"form": form})

        response = redirect('dashboard')
        response['Location'] += f'?t={str(teacher.id)}'
        return response


class DashboardView(View):

    template_name = 'dashboard.html'

    @teacher_authenticate
    def get(self, request: HttpRequest, teacher: Teacher) -> HttpResponse:
        """
        Load al the courses the teacher is giving
        :param request:
        :param teacher:
        :return:
        """
        courses = Course.objects.filter(teacher=teacher)
        return render(request, self.template_name, context={
            'teacher_id': teacher.id,
            'courses': courses
        })


class CourseView(View):

    template_name = 'course.html'

    @teacher_authenticate
    def get(self, request: HttpRequest, course_id: str, teacher: Teacher) -> HttpResponse:
        """
        Load all the projects based on the course provided
        :param request:
        :param course_id:
        :param teacher:
        :return:
        """

        projects = Project.objects.filter(course_id=course_id)
        return render(request, self.template_name, context = {
            'teacher_id': teacher.id,
            'course_id': course_id,
            'projects': projects
        })


class ProjectView(View):
    template_name = 'project.html'

    @teacher_authenticate
    def get(self, request: HttpRequest, course_id: str, project_id: str,
            teacher: Teacher) -> HttpResponse:
        """
        Load all the studens with there grade and for the given project
        :param request:
        :param course_id:
        :param project_id:
        :param teacher:
        :return:
        """

        project = Project.objects.get(id=project_id)
        grades = project.grade_set.select_related('student').all()
        return render(request, self.template_name, context={
            'teacher_id': teacher.id,
            'course_id': course_id,
            'project': project,
            'grades': grades
        })


class GradeView(View):

    template_name = 'grade.html'
    form_class = GradeForm

    @teacher_authenticate
    def get(self, request: HttpRequest, course_id: str, project_id: str, grade_id: str,
            teacher: Teacher) -> HttpResponse:
        """
        Load all the studens with there grade and for the given project
        :param request:
        :param course_id:
        :param project_id:
        :param grade_id:
        :param teacher:
        :return:
        """
        grade = Grade.objects.get(id=grade_id)
        form = self.form_class(initial={'score': grade.score})
        return render(request, self.template_name, context={
            'teacher_id': teacher.id, 'course_id': course_id, 'project_id': project_id,
            'grade': grade, 'form': form
        })

    @teacher_authenticate
    def post(self, request: HttpRequest, course_id: str, project_id: str, grade_id: str,
             teacher: Teacher) -> HttpResponse:
        """
        Update the grade form the student for the given teacher
        :param request: 
        :param course_id: 
        :param project_id: 
        :param grade_id: 
        :param teacher: 
        :return: 
        """
        grade = Grade.objects.get(id=grade_id)
        form = self.form_class(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, context={
                'teacher_id': teacher.id, 'course_id': course_id,
                'project_id': project_id, 'grade': grade,  'form': form
        })

        grade.score = form.cleaned_data.get('score')
        grade.save()

        return render(request, self.template_name, context={
            'teacher_id': teacher.id, 'course_id': course_id, 'project_id': project_id,
            'grade': grade, 'form': form
        })