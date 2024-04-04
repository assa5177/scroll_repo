from django.shortcuts import render
from fakeapp.models import Student


def classview(request):
    student_list=Student.objects.all()
    my_dict={'student_list':student_list}
    return render(request,'fakeapp/fake.html',my_dict)


# Create your views here.
