from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'home'

urlpatterns = [
    path('home/', views.home ,name='home'),
    path('', views.home ,name='home'),
    #path('', TemplateView.as_view(template_name = "index.html")),

]
