from django.contrib import admin
from fakeapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    my_list=['name','email']
admin.site.register(Student,StudentAdmin)    