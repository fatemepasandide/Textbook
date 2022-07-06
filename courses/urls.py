from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'courses'

urlpatterns = [
  #  path('home/', views.home ,name='home'),
  #  path('course/<pk>/',views.ProductDetail.as_view() , name='product-detail'),
    path('courses/',views.CourseList.as_view() , name='courses'),

]
