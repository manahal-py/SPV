# from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from FYP_App.models import Course, Session_Year, CustomUser, Student, Staff, Subject, Staff_Notification, Student_Notification, Result
from FYP_App.models import CustomUser, Course, Session_Year, Student_Course, Student, Staff, Staff_Subject, Staff_Notification, Student_Notification, Result
from django.contrib import messages


@login_required(login_url='/')
def HOME(request ):
    return render(request, 'Student/home.html')

@login_required(login_url='/')
def NOTIFICATION(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id

        student_notify = Student_Notification.objects.filter(student_id =student_id)
    context = {
        'student_notify': student_notify,

    }
    return render(request, 'Student/notification.html', context)

@login_required(login_url='/')
def STUDENT_NOTIFY_MARK_AS_DONE(request, status):
    student_notification = Student_Notification.objects.get(id=status)
    student_notification.status = 1
    student_notification.save()

    return redirect('student_notification')


def STUDENT_INBOX(request, id):
    # print(id)
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        # print(student_id)
        student_notify = Student_Notification.objects.filter(student_id=student_id)
        # print(student_notify)

        context = {
            'student_notify': student_notify,
        }
        return render(request, 'Student/student_inbox.html', context)


def STUDENT_VIEW_RESULT(request):
    student = Student.objects.get(admin = request.user.id)

    students_course = Student_Course.objects.filter(student=student)

    result = Result.objects.filter(student_id = student)

    assignment_mark = 0
    exam_mark = 0
    quiz_mark = 0
    for i in result:
        assignment_mark = i.assignment_marks
        quiz_mark = i.quiz_marks
        exam_mark = i.exam_marks
    assignment_mark_percent = round((assignment_mark / 10) * 100, 2)
    quiz_mark_percent = round((quiz_mark / 10) * 100, 2)
    exam_mark_percent = round((exam_mark / 80) * 100, 2)
    # print(assignment_mark_percent, " %")
    # print(quiz_mark_percent, " %")
    # print(exam_mark_percent, " %")

    marks = (assignment_mark) + (quiz_mark) + (exam_mark)
    total_marks_percent = round((marks / 100) * 100, 2)
    # print("Total %",  total_marks_percent, " %")


    context = {
        'result': result,
        'marks': marks,
        'student': student,
        'students_course': students_course,
        'assignment_mark_percent': assignment_mark_percent,
        'quiz_mark_percent': quiz_mark_percent,
        'exam_mark_percent': exam_mark_percent,
        'total_marks_percent': total_marks_percent,
        # 'stu_result_week': stu_result_week,
    }
    return render(request, 'Student/view_result.html', context)