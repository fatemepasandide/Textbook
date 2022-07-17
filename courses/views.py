from django.shortcuts import  render
from django.views.generic import  ListView
from .models import Course , SubCourse
from teacher.models import Teacher


# courses is displayed as a list
class CourseList(ListView):
    model = Course
    template_name = 'course/course.html'

# sub courses is displayed as a list

def courseDetail(request,coursename):
    course_name = Course.objects.filter(name=coursename)
    c_id=course_name[0].id 
    sub_course =SubCourse.objects.filter(course_id=c_id) 


    contex = {
        'sub_course' : sub_course,
        'course_name' :course_name,

      }
   
    return render(request, 'course/course-detail.html',contex)


# sub courses is displayed with detail

def courseContent(request,coursename,pk):
    sub_course_detail = SubCourse.objects.filter(pk=pk)
    course_name = Course.objects.filter(name=coursename)
    c_id=course_name[0].id
    lessons =SubCourse.objects.filter(course_id=c_id)

    course = Course.objects.all()
    teacher = Teacher.objects.all()
    


    contex = {
        'sub_course_detail' : sub_course_detail,
        'course_name' :course_name,
        'course' : course,
        'teacher' : teacher,
        'lessons' : lessons,


      }
    return render(request, 'course/course-content.html',contex)
