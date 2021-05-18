from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.
# class Post(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

class School(models.Model):
    name = models.CharField(max_length= 400)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length= 50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Certificate_Type(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name

class Grade(models.Model):
    type= models.IntegerField()

    def __str__(self):
        return '%d' % (self.type)


class Student(models.Model):
    school = models.ForeignKey(School, on_delete= models.CASCADE)
    department = models.ForeignKey(Department, on_delete= models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete= models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_Type, on_delete= models.CASCADE)
    full_name = models.CharField(max_length= 50)
    year_of_graduation = models.DateField()
    #year_of_graduation = models.DateField(default= datetime.today)

    
    def __str__(self):
        return self.full_name

