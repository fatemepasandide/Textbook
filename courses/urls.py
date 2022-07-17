from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'courses'

urlpatterns = [

  path('courses/',views.CourseList.as_view() , name='courses'),
  path('courses/<str:coursename>/',views.courseDetail , name='course-detail'),
  path('courses/<str:coursename>/<pk>/',views.courseContent , name='course-content'),
  #path('coursesdetail/<pk>',views.CourseDetail.as_view() , name='course-detail'),
  #path('coursecontent/',views.SubCourseDetail.as_view() , name='course-content'),
#  path('coursesdetail/<pk>',views.courseDetail , name='course-detail'),


]
