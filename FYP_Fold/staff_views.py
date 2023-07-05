# from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from FYP_App.models import Course, Session_Year, CustomUser, Student, Staff, Subject, Staff_Notification, Student_Notification, Result
# from FYP_App.models import CustomUser, Course, Session_Year, Student_Course, Student, Staff, Staff_Subject, Staff_Notification, Student_Notification, Result
from FYP_App.models import CustomUser, Class, Student_Class, Course, Class_Course, Session_Year, Student_Course, Student, Staff, Staff_Subject, Staff_Notification, Student_Notification, Result
from django.contrib import messages
# from django.utils.datetime_safe import datetime
from datetime import datetime, timedelta


@login_required(login_url='/')
def HOME(request ):
    return render(request, 'Staff/home.html')

@login_required(login_url='/')
def NOTIFICATION(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        staff_notify = Staff_Notification.objects.filter(staff_id = staff_id)

    context = {
        'staff_notify': staff_notify,

    }
    return render(request, 'Staff/notification.html', context)

@login_required(login_url='/')
def STAFF_NOTIFY_MARK_AS_DONE(request, status):
    staff_notification = Staff_Notification.objects.get(id = status)
    staff_notification.status = 1
    staff_notification.save()

    return redirect('staff_notification')


@login_required(login_url='/')
def STAFF_INBOX(request, id):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        staff_notify = Staff_Notification.objects.filter(staff_id=staff_id)

        context = {
            'staff_notify': staff_notify,
        }
        return render(request, 'Staff/staff_inbox.html', context)


# -------Result Portion -----
@login_required(login_url='/')
def STAFF_ADD_RESULT(request):
    staff = Staff.objects.get(admin=request.user.id)
    staff_subjects = Staff_Subject.objects.filter(staff_id=staff)

    for ss in staff_subjects:
        # print(ss)
        # print(ss.course.name)
        cls_course = Class_Course.objects.filter(course=ss.course.id)
        # print(cls_course)
        # for i in cls_course:
        #     print(i.course.name, i.class_ref)
        # print(cls_course.class_ref)
    # session_year = []
    # for i in staff_subjects:
    #     student_course_id = i.course.id
    #     students_course = Student_Course.objects.filter(course=student_course_id)
    #     # print(students_course)
    #     stu_list=[]
    #     for i in students_course:
    #         stu_id = i.student.id
    #         students = Student.objects.get(id=stu_id)
    #         stu_list.append(students)
    #
    #         stu_ses = students.session_year_id
    #         if stu_ses not in session_year:
    #             session_year.append(stu_ses)
    #         else:
    #             pass

    action = request.GET.get('action')
    get_subject = None
    get_class = None
    stu_cls = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            class_id = request.POST.get('class_id')
            if subject_id == '' or class_id == '':
                messages.warning(request, "Please Choose Subject & Class")
                return redirect('staff_add_result')
            else:
                get_subject = Staff_Subject.objects.get(id=subject_id)
                get_class = Class_Course.objects.get(id=class_id)
                print(get_class.class_ref, get_class.class_ref.id)

                stu_cls = Student_Class.objects.filter(class_name= get_class.class_ref)

    context = {
        'staff_subjects': staff_subjects,
        'cls_course': cls_course,
        # 'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_class': get_class,
        # 'get_session': get_session,
        'stu_cls': stu_cls,
        # 'stu_list': stu_list,
    }

    return render(request, 'Staff/add_result.html', context)


@login_required(login_url='/')
def STAFF_SAVE_RESULT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        # session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        # print(student_id)
        assignment_mark = request.POST.get('assignment_mark')
        quiz_mark = request.POST.get('quiz_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(id = student_id)
        # print(get_student)
        get_subject = Staff_Subject.objects.get(id=subject_id)
        # print(get_subject, get_subject.id)
        if int(assignment_mark) > 10:
            messages.warning(request, "Assignment marks should be less than 11")
            return redirect('staff_add_result')
        elif int(quiz_mark) > 11:
            messages.warning(request, "Quiz marks should be less than 11")
            return redirect('staff_add_result')
        elif int(Exam_mark) > 80:
            messages.warning(request, "Exam marks should be less than 80")
            return redirect('staff_add_result')
        else:
            pass


        check_exist = Result.objects.filter(subject_id=get_subject.id, student_id=get_student, created_at = datetime.now().date()).exists()
        # check_res = Result.objects.filter(subject_id=get_subject.id, student_id=get_student).exists()
        if check_exist:
            result = Result.objects.get( subject_id=get_subject.id, student_id=get_student, created_at = datetime.now().date())
            result.student_id=get_student
            result.subject_id=get_subject
            result.assignment_marks = assignment_mark
            result.exam_marks = Exam_mark
            result.quiz_marks = quiz_mark
            result.save()
            messages.success(request, "Successfully Updated Result")
            return redirect('staff_add_result')
        else:
            result = Result(student_id=get_student, subject_id=get_subject, exam_marks=Exam_mark,
                                assignment_marks=assignment_mark, quiz_marks=quiz_mark)
            result.save()
            messages.success(request, "Successfully Added Result")
            return redirect('staff_add_result')
    # return redirect('staff_add_result')


@login_required(login_url='/')
def STAFF_VIEW_RESULT(request):
    staff = Staff.objects.get(admin=request.user.id)
    subjects = Staff_Subject.objects.filter(staff_id=staff)
    cls = None
    for i in subjects:
        print(i.course.name, i.id)
        sub =i.course.id
        cls = Class_Course.objects.filter(course = sub)
        # print(cls)

    action = request.GET.get('action')
    get_subject = None
    get_class = None
    stu_list = None
    students_course = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            class_id = request.POST.get('class_id')
            print(subject_id)
            if subject_id == '-- Select Subject--' or class_id == '-- Select Class--':
                messages.warning(request, "Please Choose Subject & Class")
                return redirect('staff_view_result')
            else:
                get_subject = Staff_Subject.objects.get(id=subject_id)
                get_class = Class.objects.get(id=class_id)
                students_course = Student_Class.objects.filter(class_name=get_class)
                for i in students_course:
                    print(i, i.student.id)

    context = {
        'subjects': subjects,
        'cls': cls,
        'action': action,
        'get_subject': get_subject,
        'get_class': get_class,
        'students_course': students_course,
        'stu_list': stu_list,

    }

    return render(request, 'Staff/view_result_staff.html', context)


@login_required(login_url='/')
def STAFF_VIEW_RESULT_STUDENT(request , id, cid):
    sub = cid
    result = Result.objects.filter(student_id=id)
    stu = Student.objects.filter(id = id)

    cls_course = None
    for i in stu:
        # print(i.id, i)
        stu_cls = Student_Class.objects.filter(student=i.id)
        # print(stu_cls)
        for i in stu_cls:
            # print(i.class_name)
            cls_course = Class_Course.objects.filter(class_ref=i.class_name)
        # print(cls_course)

    assignment_mark = 0
    exam_mark = 0
    quiz_mark = 0
    for i in result:
        assignment_mark = i.assignment_marks
        quiz_mark = i.quiz_marks
        exam_mark = i.exam_marks
    assignment_mark_percent = assignment_mark/10*100
    quiz_mark_percent = quiz_mark/10*100
    exam_mark_percent =exam_mark/80*100
    # print(assignment_mark_percent, " %")
    # print(quiz_mark_percent, " %")
    # print(exam_mark_percent, " %")

    marks = assignment_mark + quiz_mark + exam_mark
    total_marks_percent =marks/100*100
    # print("Total %",  total_marks_percent, " %")
    student = Student.objects.filter(id = id)

    # Fetch weekly result

    context = {
        'result': result,
        'sub': sub,
        'marks': marks,
        'student': student,
        'cls_course': cls_course,
        'assignment_mark_percent': assignment_mark_percent,
        'quiz_mark_percent': quiz_mark_percent,
        'exam_mark_percent': exam_mark_percent,
        'total_marks_percent': total_marks_percent,
        # 'stu_result_week': stu_result_week,

    }
    return render(request, 'Staff/student_result.html', context)


@login_required(login_url='/')
def STAFF_EDIT_RESULT_STUDENT(request, id, date, subid):
    student = Student.objects.filter(id=id)
    cls = Student_Class.objects.filter(student=id)

    result = Result.objects.filter(student_id=id, created_at=date, subject_id=subid)
    for i in result:
        sub = i.subject_id.name
        stu = i.student_id

    context = {
            'student': student,
            'cls': cls,
            'sub': sub,
            'stu': stu,
            'result': result,


    }
    return render(request, 'Staff/staff_edit_result.html', context)


@login_required(login_url='/')
def STAFF_UPDATE_RESULT_STUDENT(request):
    if request.method == "POST":
        result_id = request.POST.get('result_id')
        date = request.POST.get('date')
        # print(date)
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        # session_year_id = request.POST.get('session_year_id')
        assignment_mark = request.POST.get('assignment_mark')
        quiz_mark = request.POST.get('quiz_mark')
        Exam_mark = request.POST.get('Exam_mark')


        get_student = Student.objects.get(id=student_id)
        # print(get_student)
        get_subject = Staff_Subject.objects.get(id=subject_id)
        # print(get_subject, get_subject.id)
        if int(assignment_mark) > 10:
            messages.warning(request, "Assignment marks should be less than 11")
            return redirect('staff_edit_result_student', student_id, date, subject_id)
        elif int(quiz_mark) > 10:
            messages.warning(request, "Quiz marks should be less than 11")
            return redirect('staff_edit_result_student', student_id, date, subject_id)
        elif int(Exam_mark) > 80:
            messages.warning(request, "Exam marks should be less than 81")
            return redirect('staff_edit_result_student', student_id, date, subject_id)
        else:
            pass

        check_exist = Result.objects.filter(subject_id=get_subject.id, student_id=get_student,
                                            created_at=datetime.now().date()).exists()
        # check_res = Result.objects.filter(subject_id=get_subject.id, student_id=get_student).exists()
        if check_exist:
            result = Result.objects.get(subject_id=get_subject.id, student_id=get_student,
                                        created_at=datetime.now().date())
            result.student_id = get_student
            result.subject_id = get_subject
            result.assignment_marks = assignment_mark
            result.exam_marks = Exam_mark
            result.quiz_marks = quiz_mark
            result.save()
            messages.success(request, "Successfully Updated Result")
            return redirect('staff_view_result')
        else:
            messages.warning(request, "Student Not founded/updated")
            return redirect('staff_view_result')

    return render(request, 'Staff/view_result_staff.html')


def STAFF_DELETE_RESULT_STUDENT(request, id):
    result = Result.objects.filter(id = id)
    result.delete()
    messages.success(request, "Result Deleted Successfully")
    return render(request, 'Staff/view_result_staff.html')

def STAFF_VIEW_RESULT_CHART(request):
    return render(request, 'Staff/indv_result_charts.html')


