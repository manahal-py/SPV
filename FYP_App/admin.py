from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser, UserModel)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
# admin.site.register(Student_Course)
admin.site.register(Staff)
admin.site.register(Staff_Subject)
admin.site.register(Staff_Notification)
admin.site.register(Student_Notification)
admin.site.register(Result)
admin.site.register(Class)
admin.site.register(Student_Class)
admin.site.register(Class_Course)