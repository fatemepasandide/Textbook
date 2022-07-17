from .models import Teacher
from django.views.generic import  ListView


class TeacherList(ListView):
    model = Teacher
    template_name = 'teacher.html'