from django.shortcuts import render
from .models import Python_Jun

# Create your views here.
def Show_StudentList(request):
    Student = Python_Jun.objects.all()
    return render(request,'CRUD.html',{Student:'Student'})
