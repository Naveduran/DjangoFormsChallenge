from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('id', 'name', 'phone')


class CourseAssignForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.values_list(
            'name', flat=True).order_by('name'))

    class Meta:
        model = Student
        fields = ('courses', 'student')
