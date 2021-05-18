from django.contrib import admin
from .models import Certificate_Type, Department, Faculty, Grade, School, Student

# Register your models here.
# admin.site.register(Post)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(Certificate_Type)


