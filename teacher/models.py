from django.db import models

class Teacher(models.Model):
    name            = models.CharField(max_length=20)
    image_teacher   = models.ImageField(upload_to='teacher')
    about           = models.TextField(max_length=300)

    def __str__(self):
        return self.name