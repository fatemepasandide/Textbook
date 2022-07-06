from django.views.generic import DetailView , ListView
from .models import Course

# product is displayed as list
class CourseList(ListView):
    model = Course
    template_name = 'course/course.html'

# product is displayed with details
class CourseDetail(DetailView):
    model = Course
    template_name = 'course/course-detail.html'