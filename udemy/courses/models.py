import uuid
from django.db import models

# Create your models here.

class Sector(models.Model):
    name=models.CharField(max_length=255)
    sector_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    ralated_course=models.ManyToManyField('Course')
    sector_image = models.ImageField(upload_to='sector_image')
     

class Course(models.Model):
    title=models.CharField(max_length=255, null=True)
    description: models.TextField(null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey()
    language=models.CharField(max_length=50)
    course_section = models.ManyToManyField('CourseSection')
    comments = models.ManyToManyField('Comment')
    image_url=models.ImageField(upload_to='course_images')
    course_uuid=models.UUIDField(default=uuid.uuid4, unique=True)
    price=models.DecimalField(max_digits=5, decimal_places=2)


class CourseSection(models.Model):
    section_title= models.CharField(max_length=255)
    episodes=models.ManyToManyField('Eposide')

class Episode(models.Model):
    title=models.CharField(max_length=255)
    file=models.FileField(upload_to='course_videos')
    length=models.DecimalField(max_digits=10, decimal_places=2)


class Comment(models.Model):
    # user=models.ForeignKey()
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)