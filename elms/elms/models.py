from django.db import DEFAULT_DB_ALIAS, models
from django.utils import timezone
from django.contrib.auth.models import User


class announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(default= timezone.now)

class practice(models.Model):
    topic = models.CharField(max_length=100)
    createdAt = models.DateTimeField(default= timezone.now)
    content = models.TextField()
    file = models.FileField()

class HW(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    marks = models.FloatField()
    createdAt = models.DateTimeField(default= timezone.now)
    duration = models.CharField(max_length=20)

class CT(models.Model):
    title = models.CharField(max_length=100)
    details= models.TextField()
    marks = models.FloatField()
    createdAt = models.DateTimeField(default= timezone.now)
    duration = models.CharField(max_length=20)
    

class course(models.Model):
    course_title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=8)
    content = models.TextField()
    section = models.CharField(max_length=3)