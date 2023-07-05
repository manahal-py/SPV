from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from FYP_App.models import Course, Session_Year, CustomUser, Student, Staff, Subject, Staff_Notification, Student_Notification, Result
from FYP_App.models import CustomUser, Class, Student_Class, Course, Class_Course, Session_Year, Student_Course, Student, Staff, Staff_Subject, Staff_Notification, Student_Notification, Result
from django.contrib import messages


# from S_P_visualizer.S_P_V import admin


@login_required(login_url='/')
def HOME(request ):
    student = Student.objects.all()
    student_count = Student.objects.all().count()
    course_count = Course.objects.all().count()
    staff_count = Staff.objects.all().count()
    staff_subject_count = Staff_Subject.objects.all().count()
    session_year_count = Session_Year.objects.all().count()
    class_count = Class.objects.all().count()
    stu_class_count = Student_Class.objects.all().count()
    session_year = Session_Year.objects.all()
    # stu_cls =Student_Class.objects.all()

    male = []
    female = []
    for i in student:
        stu_male_count_s = Student.objects.filter(created_at=i.created_at, gender='Male').count()
        stu_female_count_s = Student.objects.filter(created_at=i.created_at, gender='Female').count()
        male.append(stu_male_count_s)
        female.append(stu_female_count_s)
        male_set = set(male)
        female_set = set(female)

    male= list(male_set)
    female= list(female_set)


    context = {
        'student': student,
        'student_count': student_count,
        'course_count': course_count,
        'staff_count': staff_count,
        'staff_subject_count': staff_subject_count,
        'session_year_count': session_year_count,
        'class_count': class_count,
        'stu_class_count': stu_class_count,
        'session_year': session_year,
        'male': male,
        'female': female,
    }
    return render(request, 'HOD/home.html', context)


# Student Portion
@login_required(login_url='/')
def ADD_STUDENT(request):

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken !')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken !')
            return redirect('add_student')
        else:
            user = CustomUser(
                profile_pic=profile_pic,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                user_type='3',
            )
            user.set_password(password)
            user.save()


            student = Student(
                admin=user,
                address=address,
                gender=gender,
            )
            student.save()
            messages.success(request, user.first_name + " " + user.last_name +' are Successfully Added !')
            return redirect('view_student')

    return render(request, 'HOD/add_student.html')


@login_required(login_url='/')
def VIEW_STUDENT(request):
    student_courses = Student_Course.objects.all()

    student = Student.objects.all()
    stu_class = Student_Class.objects.all()

    context = {
        'student': student,
        'student_courses': student_courses,
        'stu_class': stu_class,
    }
    return render(request, 'HOD/view_student.html', context)


@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id=id)
    session_year = Session_Year.objects.all()
    context = {
        'student': student,
        'session_year': session_year,
    }
    return render(request, 'HOD/edit_student.html', context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        # print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        student = Student.objects.get(admin=student_id)
        # print(student.admin.first_name)
        # print(student.id)
        if gender=="" :
            messages.warning(request, "Please Choose Gender!")
            return redirect('edit_student', student.id)
        else:
            user = CustomUser.objects.get(id = student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username

            if password != None and password != "":
                user.set_password(password)
            if profile_pic != None and profile_pic != "":
                user.profile_pic = profile_pic
            user.save()


            student = Student.objects.get(admin = student_id)
            student.address = address
            student.gender = gender

            student.save()
            messages.success(request, 'Student Updated Successfully !')
            return redirect('view_student')

    return render(request, 'HOD/edit_student.html')


@login_required(login_url='/')
def DELETE_STUDENT(request, admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request, 'Student Deleted Successfully !')
    return redirect('view_student')


@login_required(login_url='/')
def ADD_STAFF(request):
    # course = Course.objects.all()
    # session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email = email).exists():
            messages.warning(request, 'Email is already taken !')
            return redirect('add_staff')
        if CustomUser.objects.filter(username = username).exists():
            messages.warning(request, 'Email is already taken !')
            return redirect('add_staff')
        else:
            user = CustomUser(
                profile_pic = profile_pic,
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                user_type = '2',
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                address=address,
                gender=gender,
            )
            staff.save()
            messages.success(request, user.first_name + " " + user.last_name + ' are Successfully Added !')
            return redirect('view_staff')
        # print(profile_pic,first_name,last_name,email,username,password,address,gender)
    return render(request, 'HOD/add_staff.html')


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff,
    }
    return render(request, 'HOD/view_staff.html', context)


@login_required(login_url='/')
def EDIT_STAFF(request, id):
    staff = Staff.objects.filter(id=id)
    context = {
        'staff': staff,
    }
    return render(request, 'HOD/edit_staff.html', context)


@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        staff = Staff.objects.get(admin = staff_id)
        if gender=="":
            messages.warning(request, "Please Choose Gender")
            return redirect('edit_staff', staff.id)
        else:
            user = CustomUser.objects.get(id = staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username

            if password != None and password != "":
                user.set_password(password)
            if profile_pic != None and profile_pic != "":
                user.profile_pic = profile_pic
            user.save()


            staff = Staff.objects.get(admin = staff_id)
            staff.address = address
            staff.gender = gender
            # if gender != None and gender != "":
            #     student.gender = gender

            staff.save()
            messages.success(request, 'Record Updated Successfully !')
            return redirect('view_staff')
    return render(request, 'HOD/edit_staff.html')


@login_required(login_url='/')
def DELETE_STAFF(request , admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, 'Record Deleted Successfully !')
    return redirect('view_staff')


# ------------Course Portion-------------
@login_required(login_url='/')
def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request, 'Course are Successfully Added!')
        return redirect('view_course')
    return render(request, 'HOD/add_course.html')


@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'HOD/view_course.html', context)


@login_required(login_url='/')
def EDIT_COURSE(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, 'HOD/edit_course.html', context)


@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')
        if course_name=="" or course_name==None:
            messages.warning(request, "Please Enter Course Name!")
            return redirect('edit_course', course_id)
        else:
            course = Course.objects.get(id = course_id)
            course.name = course_name
            course.save()

            messages.success(request, 'Course Updated Successfully !')
            return redirect('view_course')

    return render(request, 'HOD/edit_course.html')


@login_required(login_url='/')
def DELETE_COURSE(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request, 'Course Deleted Successfully !')
    return redirect('view_course')




# --------Subject Function Portion------------

@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff = Staff.objects.all()
    # classes = Class.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        # class_id = request.POST.get('class_id')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        # classes = Class.objects.get(id = class_id)
        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        check_name = Staff_Subject.objects.filter(name=subject_name).exists()
        check_staff = Staff_Subject.objects.filter(staff=staff).exists()
        check_course = Staff_Subject.objects.filter(course=course).exists()
        if check_name:
            messages.warning(request, "Subject Name / Code Already Assigned!")
            return redirect('add_subject')
        elif check_staff:
            messages.warning(request, "Staff Already Teach Someone course!")
            return redirect('add_subject')
        elif check_course:
            messages.warning(request, "Course Already Assigned to other Staff!")
            return redirect('add_subject')
        else:
            staff_subject = Staff_Subject(
                name  = subject_name,
                course = course,
                staff = staff,
                # class_name= classes,
            )
            staff_subject.save()
            messages.success(request, 'Subject Added Successfully !')
            return redirect('view_subject')

    context = {
        'course':course,
        'staff':staff,
        # 'classes':classes,
    }
    return render(request, 'HOD/add_subject.html', context)


@login_required(login_url='/')
def VIEW_SUBJECT(request):
    staff_subject = Staff_Subject.objects.all()
    # course = Course.objects.all()
    # staff = Staff.objects.all()
    context = {
        'staff_subject': staff_subject,
        # 'course': course,
        # 'staff': staff,
    }
    return render(request, 'HOD/view_subject.html', context)


@login_required(login_url='/')
def EDIT_SUBJECT(request , id):
    staff_subject = Staff_Subject.objects.get(id=id)
    print(staff_subject.staff)

    course = []
    staff_course_check = Course.objects.all()
    for i in staff_course_check:
        if staff_subject.course.name == i.name:
            course.append(i)
        else:
            pass
    staff= []
    staff_check = Staff.objects.all()
    for i in staff_check:
        if staff_subject.staff.admin.username == i.admin.username:
            pass
        else:
            staff.append(i)

    context = {
        'staff_subject': staff_subject,
        'course': course,
        'staff': staff,
    }
    return render(request, 'HOD/edit_subject.html', context)


@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        subject_id = request.POST.get('subject_id')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')


        if subject_name=="" or course_id=="" or staff_id=="":
            messages.warning(request, "Please Enter All Data")
            return redirect('edit_subject', subject_id)

        staff = Staff.objects.get(id=staff_id)
        course = Course.objects.get(id=course_id)

        staff_subject = Staff_Subject(
            id = subject_id,
            name = subject_name,
            course = course,
            staff = staff,
        )
        staff_subject.save()

        messages.success(request, 'Course Updated Successfully !')
        return redirect('view_subject')

    return render(request, 'HOD/edit_subject.html')


@login_required(login_url='/')
def DELETE_SUBJECT(request , id):
    staff_subject = Staff_Subject.objects.get(id = id)
    staff_subject.delete()
    messages.success(request, 'Subject Deleted Successfully !')
    return redirect('view_subject')


# -----------Session Portion------------
@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == "POST":
        start_date = request.POST.get('start_date')

        if len(start_date) < 4 or len(start_date) > 4 or start_date==None:
            messages.warning(request, "Please enter valid session with proper length! like 2023")
            return redirect("add_session")
        else:
            session_year = Session_Year(
                session=start_date,
            )
            session_year.save()
            messages.success(request, 'Session are Successfully Added!')
            return redirect('add_session')
    return render(request, 'HOD/add_session.html')


@login_required(login_url='/')
def VIEW_SESSION(request):
    session_year = Session_Year.objects.all()
    context = {
        'session_year': session_year,
    }
    return render(request, 'HOD/view_session.html', context)


@login_required(login_url='/')
def EDIT_SESSION(request ,id):
    session_year = Session_Year.objects.filter(id=id)
    context = {
        'session_year': session_year,
    }
    return render(request, 'HOD/edit_session.html', context)


@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == "POST":
        start_date = request.POST.get('start_date')
        session_id = request.POST.get('session_id')

        # session = Session_Year.objects.get(id=session_id)
        if len(start_date) < 4 or len(start_date) > 4 or start_date==None:
            messages.warning(request, "Please enter valid session with proper length! like 2023")
            return redirect("edit_session", session_id)
        else:
            session = Session_Year(
                id=session_id,
                session=start_date,
            )
            session.save()

        messages.success(request, 'Session Updated Successfully !')
        return redirect('view_session')
    return render(request, 'HOD/edit_session.html')


@login_required(login_url='/')
def DELETE_SESSION(request , id):
    session = Session_Year.objects.get(id=id)
    session.delete()
    messages.success(request, 'Session Deleted Successfully !')
    return redirect('view_session')


#Student  Class Portions
@login_required(login_url='/')
def ADD_STUDENT_CLASS(request):
    # course = Course.objects.all()
    student = Student.objects.all()
    classes = Class.objects.all()

    for s in student:
        print(s.created_at)


    if request.method == "POST":
        class_id = request.POST.get('class_id')
        stu_id = request.POST.get('stu_id')

        stu = Student.objects.get(id=stu_id)
        cls = Class.objects.get(id=class_id)

        check_stu = Student_Class.objects.filter(student=stu).exists()
        if check_stu:
            messages.warning(request, "Student Already Enrolled in other class!")
            return redirect('add_student_class')
        else:
            stu_class = Student_Class(
                student = stu,
                class_name=cls,
            )
            stu_class.save()
            messages.success(request, 'Student Class Added Successfully !')
            return redirect('add_student_class')

    context = {
        # 'course': course,
        'classes': classes,
        'student': student,
    }
    return render(request, 'HOD/add_stu_class.html', context)


@login_required(login_url='/')
def VIEW_STUDENT_CLASS(request):
    stu_class = Student_Class.objects.all()
    context = {
        'stu_class': stu_class,
    }
    return render(request, 'HOD/view_stu_class.html', context)


@login_required(login_url='/')
def EDIT_STUDENT_CLASS(request , id):
    stu_class = Student_Class.objects.filter(id = id)
    for sc in stu_class:
        stu_cls_id=sc.id
        stu_cls = sc.class_name
        # print(sc.student, sc.student.id)
    classes = []
    cls = Class.objects.all()
    for i in cls:
        if i == stu_cls:
            pass
        else:
            classes.append(i)


    context = {
        'stu_class': stu_class,
        'classes': classes,
        'stu_cls_id': stu_cls_id,
        # 'cls': cls,
    }
    return render(request, 'HOD/edit_stu_class.html', context)

@login_required(login_url='/')
def UPDATE_STUDENT_CLASS(request):
    if request.method == "POST":
        stu_cls_id = request.POST.get('stu_cls_id')
        stu_id = request.POST.get('stu_id')
        cls_id = request.POST.get('cls_id')


        if cls_id=="" or stu_id=="":
            messages.warning(request, "Please Choose Student & Class!")
            return redirect('edit_student_class', stu_cls_id)
        stu = Student.objects.get(id=stu_id)
        clas = Class.objects.get(id=cls_id)
        student_cls = Student_Class(
            id = stu_cls_id,
            class_name = clas,
            student = stu,
        )
        student_cls.save()

        messages.success(request, 'Student Class Updated Successfully !')
        return redirect('view_student_class')

    return render(request, 'HOD/edit_stu_class.html')


@login_required(login_url='/')
def DELETE_STUDENT_CLASS(request , id):
    stu_class = Student_Class.objects.filter(id = id)
    stu_class.delete()
    messages.success(request, 'Student Class Deleted Successfully !')
    return redirect('view_student_class')


# Class Subjects Portions
@login_required(login_url='/')
def ADD_CLASS_COURSE(request):
    course = Course.objects.all()
    # student = Student.objects.all()
    classes = Class.objects.all()

    if request.method == "POST":
        course_id = request.POST.get('course_id')
        class_id = request.POST.get('class_id')

        course = Course.objects.get(id=course_id)
        cls = Class.objects.get(id=class_id)
        check_exist = Class_Course.objects.filter(course=course_id, class_ref=cls).exists()
        if check_exist:
            messages.warning(request, "Class Course Already Exist")
            return redirect('add_class_course')
        else:
            cls_course = Class_Course(
                class_ref = cls,
                course=course,
            )
            cls_course.save()
            messages.success(request, 'Class Course Added Successfully !')
            return redirect('add_class_course')

    context = {
        'course': course,
        'classes': classes,
        # 'stu': student,
    }
    return render(request, 'HOD/add_class_course.html', context)


@login_required(login_url='/')
def VIEW_CLASS_COURSE(request):
    cls_course = Class_Course.objects.all()
    context = {
        'cls_course': cls_course,
    }
    return render(request, 'HOD/view_class_course.html', context)


@login_required(login_url='/')
def EDIT_CLASS_COURSE(request , id):
    cls_course = Class_Course.objects.get(id = id)
    cls_name = cls_course.class_ref

    course = []
    course_check = Course.objects.all()
    for i in course_check:
        if cls_course.course.name == i.name:
            pass
        else:
            course.append(i)

    context = {
        'cls_name': cls_name,
        'course': course,
        'cls_course': cls_course,
    }
    return render(request, 'HOD/edit_class_course.html', context)


@login_required(login_url='/')
def UPDATE_CLASS_COURSE(request):
    if request.method == "POST":
        class_course_id = request.POST.get('class_course_id')
        cls_id = request.POST.get('cls_id')
        course_id = request.POST.get('course_id')


        if course_id=="" or cls_id=="":
            messages.warning(request, "Please Choose Class & Course !")
            return redirect('edit_class_course', class_course_id)
        check_exist = Class_Course.objects.filter(course=course_id, class_ref= cls_id).exists()
        if check_exist:
             messages.warning(request, "Class Course Already Exist")
             return redirect('edit_class_course', class_course_id)
        else:
            classes = Class.objects.get(id=cls_id)
            course = Course.objects.get(id=course_id)
            cls_course = Class_Course(
                id = class_course_id,
                course = course,
                class_ref = classes,
            )
            cls_course.save()

            messages.success(request, 'Class Course Updated Successfully !')
            return redirect('view_class_course')

    return render(request, 'HOD/edit_class_course.html')


@login_required(login_url='/')
def DELETE_CLASS_COURSE(request , id):
    cls_course = Class_Course.objects.get(id = id)
    cls_course.delete()
    messages.success(request, 'Class Course Deleted Successfully !')
    return redirect('view_class_course')


# -----------Class Portions----------
@login_required(login_url='/')
def ADD_CLASS(request):
    session = Session_Year.objects.all()

    if request.method == "POST":
        class_name = request.POST.get('class_name')
        session_id = request.POST.get('session_id')
        print(class_name, session_id)

        sessions = Session_Year.objects.get(id=session_id)

        check_exist = Class.objects.filter(class_name=class_name, session_id=sessions).exists()
        if check_exist:
            messages.warning(request, "Class Already Exist")
            return redirect('add_class')
        else:
            cls = Class(
                class_name = class_name,
                session_id=sessions,
            )
            cls.save()
            messages.success(request, 'Class Added Successfully !')
            return redirect('add_class')

    context = {
        'session': session,
    }
    return render(request, 'HOD/add_class.html', context)

@login_required(login_url='/')
def VIEW_CLASS(request):
    cls = Class.objects.all()
    context = {
        'cls': cls,
    }
    return render(request, 'HOD/view_class.html', context)

@login_required(login_url='/')
def EDIT_CLASS(request , id):
    cls = Class.objects.get(id = id)
    cls_sesion = cls.session_id
    cls_name = cls.class_name

    session = []
    session_check = Session_Year.objects.all()
    for i in session_check:
        if cls_sesion == i:
            pass
        else:
            session.append(i)

    context = {
        'cls': cls,
        'session': session,
        'cls_name': cls_name,
    }
    return render(request, 'HOD/edit_class.html', context)

@login_required(login_url='/')
def UPDATE_CLASS(request):
    if request.method == "POST":
        class_id = request.POST.get('class_id')
        class_name = request.POST.get('class_name')
        session_id = request.POST.get('session_id')


        if class_name=="" or session_id=="":
            messages.warning(request, "Please Choose Class & Session!")
            return redirect('edit_class', class_id)
        check_exist = Class.objects.filter(class_name=class_name, session_id= session_id).exists()
        if check_exist:
             messages.warning(request, "Class Already Exist")
             return redirect('edit_class', class_id)
        else:
            # classes = Class.objects.get(id=class_id)
            sessions = Session_Year.objects.get(id=session_id)
            cls = Class(
                id = class_id,
                class_name = class_name,
                session_id = sessions,
            )
            cls.save()

            messages.success(request, 'Class Updated Successfully !')
            return redirect('view_class')

    return render(request, 'HOD/edit_class.html')


@login_required(login_url='/')
def DELETE_CLASS(request , id):
    cls = Class.objects.get(id = id)
    cls.delete()
    messages.success(request, 'Class Deleted Successfully !')
    return redirect('view_class')



# --------notification staff-------
@login_required(login_url='/')
def SEND_NOTIFICATION_STAFF(request):
    staff = Staff.objects.all()
    seen_staff_notification = Staff_Notification.objects.all()
    context = {
        'staff': staff,
        'seen_staff_notification': seen_staff_notification,
    }
    return render(request, 'HOD/send_notification_staff.html', context)


@login_required(login_url='/')
def SAVE_NOTIFICATION_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        if len(message) <=20 or message=="":
            messages.warning(request, "Please Enter at least 20 characters for message!")
            return redirect('send_notification_staff')
        else:
            staff = Staff.objects.get(admin=staff_id)

            staff_notification = Staff_Notification(
                staff_id = staff,
                message = message,
            )
            staff_notification.save()
            messages.success(request, 'Notification Send Successfully !')
            return redirect('send_notification_staff')
    return render(request, 'HOD/send_notification_staff.html')


@login_required(login_url='/')
def VIEW_NOTIFICATION_STAFF(request):
    view_staff_notification = Staff_Notification.objects.all()
    context = {
        'view_staff_notification': view_staff_notification,
    }
    return render(request, 'HOD/send_notification_staff.html', context)


@login_required(login_url='/')
def RESEND_NOTIFICATION_STAFF(request, id):
    staff_notify = Staff_Notification.objects.get(id =id)
    staff_notify.status = 0
    staff_notify.save()

    return redirect('send_notification_staff')


@login_required(login_url='/')
def SEND_NOTIFICATION_STUDENT(request):
    student = Student.objects.all()
    seen_student_notification = Student_Notification.objects.all()
    context = {
        'student': student,
        'seen_student_notification': seen_student_notification,
    }
    return render(request, 'HOD/send_notification_student.html', context)

@login_required(login_url='/')
def SAVE_NOTIFICATION_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')

        if len(message) <=20 or message=="":
            messages.warning(request, "Please Enter at least 20 characters for message!")
            return redirect('send_notification_student')
        else:
            student = Student.objects.get(admin=student_id)

            student_notification = Student_Notification(
                student_id=student,
                message=message,
            )
            student_notification.save()
            messages.success(request, 'Notification Send Successfully !')
            return redirect('send_notification_student')
    return render(request, 'HOD/send_notification_student.html')


@login_required(login_url='/')
def VIEW_NOTIFICATION_STUDENT(request):
    view_student_notification = Student_Notification.objects.all()
    context = {
        'view_student_notification': view_student_notification,
    }
    return render(request, 'HOD/send_notification_student.html', context)


@login_required(login_url='/')
def RESEND_NOTIFICATION_STUDENT(request ,id):
    student_notify = Student_Notification.objects.get(id =id)
    student_notify.status = 0
    student_notify.save()

    return redirect('send_notification_student')


@login_required(login_url='/')
def HOD_VIEW_RESULT(request):
    students = Student.objects.all()
    stu_class = []
    for i in students:
        stu_cls = Student_Class.objects.get(student= i.id)
        stu_class.append(stu_cls)
    result = Result.objects.all()

    context = {
        'students': students,
        'stu_class': stu_class,
        'result': result,
    }
    return render(request, 'HOD/hod_view_result.html', context)



@login_required(login_url='/')
def HOD_VIEW_RESULT_STUDENT(request, id):
    result = Result.objects.filter(student_id=id)
    # students_course = Student_Course.objects.filter(student=id)
    # # print(students_course)
    # # for i in students_course:
    # #     print(i.course.name)
    stu = Student.objects.filter(id=id)

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
    total_marks_percent = marks / 100 * 100
    # print("Total %",  total_marks_percent, " %")

    student = Student.objects.filter(id=id)

    context = {
        'result': result,
        # 'students_course': students_course,
        'cls_course': cls_course,
        'marks': marks,
        'student': student,
        'assignment_mark_percent': assignment_mark_percent,
        'quiz_mark_percent': quiz_mark_percent,
        'exam_mark_percent': exam_mark_percent,
        'total_marks_percent': total_marks_percent,
    }
    return render(request, 'Hod/hod_student_result.html', context)


def test(request):
    stu = Student.objects.all()
    for i in stu:
        stu_id = i.id
        stu_class = Student_Class.objects.filter(student = i)
        print(i,stu_class)
        for s in stu_class:
            print(s.class_name)
            print(s.class_name.session_year_id)
            class_cour = Class_Course.objects.filter(class_ref=s.class_name)
            print(s.class_name,class_cour)
    return HttpResponse ("This is test Page")