from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )
    user_type = models.IntegerField(choices=USER, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Session_Year(models.Model):
    session = models.CharField(max_length=4)

    def __str__(self):
        return self.session

class Class(models.Model):
    class_name= models.CharField(max_length=100)
    session_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.class_name + " - " + str(self.session_id)

class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.IntegerField()
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.created_at=datetime.now().year
        super().save(*args, **kwargs)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name




class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username + "-" + self.admin.first_name + " " + self.admin.last_name


class Student_Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.admin.first_name + " " + self.student.admin.last_name+ " - "+ self.course.name


class Class_Course(models.Model):
    class_ref = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_ref.class_name + " - " +str(self.class_ref.session_id)+ " - "+ self.course.name


class Student_Class(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.admin.first_name + " " + self.student.admin.last_name+ " - "+ self.class_name.class_name+ " - "+ str(self.class_name.session_id)


class Staff_Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    # class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name+ " -- " + self.course.name+ " -- " + self.staff.admin.first_name+ "  " + self.staff.admin.last_name


class Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.staff_id.admin.first_name  + " " + self.staff_id.admin.last_name

class Student_Notification(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.student_id.admin.first_name  + " " + self.student_id.admin.last_name


class Result(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Staff_Subject, on_delete=models.CASCADE)
    assignment_marks = models.IntegerField()
    quiz_marks = models.IntegerField()
    exam_marks = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name  + " " + self.student_id.admin.last_name+ "  -  " + self.subject_id.course.name+"  -  " + str(self.updated_at)
