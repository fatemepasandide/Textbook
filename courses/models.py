from django.db import models

class Course(models.Model):
    types =(('video', 'video'), ('booklet','booklet'),)

    name            = models.CharField(max_length=20)
    price           = models.CharField(max_length=50)
    image_course    = models.ImageField(upload_to='course')
    teacher         = models.CharField(max_length=20)
    description     = models.TextField(max_length=300)
    length          = models.CharField(max_length=15)
    course_type     = models.CharField(max_length=10,choices=types,default='booklet')


    def __str__(self):
        return self.name


class SubCourse(models.Model):
    course            = models.ForeignKey(Course,on_delete=models.CASCADE)
    sub_videos        = models.FileField(upload_to='course')
    sub_name          = models.CharField(max_length=20)
    sub_image_course  = models.ImageField(upload_to='course')
    sub_context       = models.TextField(max_length=9000)

    def __str__(self):
        return self.sub_name