from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Assignment(models.Model):
    course = models.CharField(max_length=32)

    def __str__(self):
        return self.course


class Student(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    phone = PhoneNumberField()
    courses = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name="students",
        null=True,
        blank=True)

    def ___str__(self):
        return self.name
