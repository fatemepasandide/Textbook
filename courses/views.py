from django.shortcuts import  render
from django.views.generic import  ListView
from .models import Course , SubCourse
from teacher.models import Teacher



class CourseList(ListView):
    """
    Courses is displayed as a list.
    """
    model = Course
    template_name = 'course/course.html'

def course_detail(request,coursename):
    """
    Sub courses is displayed as a list.
    """
    course_name = Course.objects.filter(name=coursename)
    c_id=course_name[0].id 
    sub_course =SubCourse.objects.filter(course_id=c_id) 


    contex = {
        'sub_course' : sub_course,
        'course_name' :course_name,

      }
   
    return render(request, 'course/course-detail.html',contex)


# 

def course_content(request,coursename,pk):
    """
    Sub courses is displayed with detail.
    """
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
