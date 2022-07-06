from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'teacher'

urlpatterns = [
    path('teacher/', views.teacher ,name='teacher'),

]
