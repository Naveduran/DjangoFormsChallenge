from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .forms import StudentForm, CourseAssignForm
from .models import Student


def HomeView(request):
    """Main menu"""
    return render(request, 'home.html')


def StudentView(request):
    """Allows creating a new student."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.data.name)
            name = form.data.name
            student = Student.objects.filter(name=name) or None
            if student:
                form = StudentForm(request.POST, instance=student)
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = StudentForm()
    return render(request, 'student.html', {'form': form})


def CourseView(request):
    """Allows asignning courses to a student."""
    students = Student.objects.all()
    if request.method == 'POST':
        form = CourseAssignForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CourseAssignForm()
    return render(request, 'course.html', {'form': form})
