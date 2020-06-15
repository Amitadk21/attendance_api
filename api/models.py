from django.db import models


# Create your models here.
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    attendance_date = models.DateField()
    student_name = models.CharField(max_length=100, default='student name')
    roll_number = models.IntegerField(default=0)
    grade = models.CharField(max_length=20)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name
