from django.shortcuts import render, get_object_or_404, redirect
from .models import Python_Jun # importing model Python_jun
from .forms import PythonForm # importing form PythonForm

# Read (List) 
def Show_StudentList(request):
    students = Python_Jun.objects.all()
    return render(request, 'CRUD.html', {'Student': students})
# Create (Add)
def Add_Student(request):
    if request.method == 'POST': #Request for adding Student
        form = PythonForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('show_students')
    else:
        form = PythonForm()
    return render(request, 'add_student.html', {'form': form})
# Update (Edit)
def Edit_Student(request, id):
    student = get_object_or_404(Python_Jun, pk=id)
    if request.method == 'POST':
        form = PythonForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_students')
    else:
        form = PythonForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

# Delete
def Delete_Student(request, id):
    student = get_object_or_404(Python_Jun, pk=id)
    student.delete()
    return redirect('show_students') 
