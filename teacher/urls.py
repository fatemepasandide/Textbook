from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('teacher/', views.TeacherList.as_view() ,name='teacher'),

]
