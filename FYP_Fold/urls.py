from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, HOD_views, staff_views, student_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('test', HOD_views.test, name="test"),

# login
    path('', views.LOGIN, name="login"),
    path('dologin', views.dologin, name="dologin"),
    path('dologout', views.dologout, name="logout"),

# Profile Update
    path('Profile', views.PROFILE, name="profile"),
    path('Profile/update', views.PROFILE_UPDATE, name="profile_update"),

# HOD Urls
    # HOD Home
    path('Hod/Home', HOD_views.HOME, name="hod_home"),

    # Add Student
    path('Hod/Student/Add', HOD_views.ADD_STUDENT, name="add_student"),
    path('Hod/Student/View', HOD_views.VIEW_STUDENT, name="view_student"),
    path('Hod/Student/Edit/<str:id>', HOD_views.EDIT_STUDENT, name="edit_student"),
    path('Hod/Student/Update', HOD_views.UPDATE_STUDENT, name="update_student"),
    path('Hod/Student/Delete/<str:admin>', HOD_views.DELETE_STUDENT, name="delete_student"),

    # Add Staff
    path('Hod/Staff/Add', HOD_views.ADD_STAFF, name="add_staff"),
    path('Hod/Staff/View', HOD_views.VIEW_STAFF, name="view_staff"),
    path('Hod/Staff/Edit/<str:id>', HOD_views.EDIT_STAFF, name="edit_staff"),
    path('Hod/Staff/Update', HOD_views.UPDATE_STAFF, name="update_staff"),
    path('Hod/Staff/Delete/<str:admin>', HOD_views.DELETE_STAFF, name="delete_staff"),

     # Add Course
    path('Hod/Course/Add', HOD_views.ADD_COURSE, name="add_course"),
    path('Hod/Course/View', HOD_views.VIEW_COURSE, name="view_course"),
    path('Hod/Course/Edit/<str:id>', HOD_views.EDIT_COURSE, name="edit_course"),
    path('Hod/Course/Update', HOD_views.UPDATE_COURSE, name="update_course"),
    path('Hod/Course/Delete/<str:id>', HOD_views.DELETE_COURSE, name="delete_course"),

    # Add Classes
    path('Hod/Class/Add', HOD_views.ADD_CLASS, name="add_class"),
    path('Hod/Class/View', HOD_views.VIEW_CLASS, name="view_class"),
    path('Hod/Class/Edit/<str:id>', HOD_views.EDIT_CLASS, name="edit_class"),
    path('Hod/Class/Update', HOD_views.UPDATE_CLASS, name="update_class"),
    path('Hod/Class/Delete/<str:id>', HOD_views.DELETE_CLASS, name="delete_class"),

    # Add Student Classes
    path('Hod/Student/Class/Add', HOD_views.ADD_STUDENT_CLASS, name="add_student_class"),
    path('Hod/Student/Class/View', HOD_views.VIEW_STUDENT_CLASS, name="view_student_class"),
    path('Hod/Student/Class/Edit/<str:id>', HOD_views.EDIT_STUDENT_CLASS, name="edit_student_class"),
    path('Hod/Student/Class/Update', HOD_views.UPDATE_STUDENT_CLASS, name="update_student_class"),
    path('Hod/Student/Class/Delete/<str:id>', HOD_views.DELETE_STUDENT_CLASS, name="delete_student_class"),

    # Add Subject
    path('Hod/Subject/Add', HOD_views.ADD_SUBJECT, name="add_subject"),
    path('Hod/Subject/View', HOD_views.VIEW_SUBJECT, name="view_subject"),
    path('Hod/Subject/Edit/<str:id>', HOD_views.EDIT_SUBJECT, name="edit_subject"),
    path('Hod/Subject/Update', HOD_views.UPDATE_SUBJECT, name="update_subject"),
    path('Hod/Subject/Delete/<str:id>', HOD_views.DELETE_SUBJECT, name="delete_subject"),

    # Add Session
    path('Hod/Session/Add', HOD_views.ADD_SESSION, name="add_session"),
    path('Hod/Session/View', HOD_views.VIEW_SESSION, name="view_session"),
    path('Hod/Session/Edit/<str:id>', HOD_views.EDIT_SESSION, name="edit_session"),
    path('Hod/Session/Update', HOD_views.UPDATE_SESSION, name="update_session"),
    path('Hod/Session/Delete/<str:id>', HOD_views.DELETE_SESSION, name="delete_session"),

    # # Student Subjects
    # path('Hod/Student/Course/Add', HOD_views.ADD_STU_COURSE, name="add_stu_course"),
    # path('Hod/Student/Course/View', HOD_views.VIEW_STU_COURSE, name="view_stu_course"),
    # path('Hod/Student/Course/Edit/<str:id>', HOD_views.EDIT_STU_COURSE, name="edit_stu_course"),
    # path('Hod/Student/Course/Update', HOD_views.UPDATE_STU_COURSE, name="update_stu_course"),
    # path('Hod/Student/Course/Delete/<str:id>', HOD_views.DELETE_STU_COURSE, name="delete_stu_course"),

    # Class Subjects
    path('Hod/Class/Course/Add', HOD_views.ADD_CLASS_COURSE, name="add_class_course"),
    path('Hod/Class/Course/View', HOD_views.VIEW_CLASS_COURSE, name="view_class_course"),
    path('Hod/Class/Course/Edit/<str:id>', HOD_views.EDIT_CLASS_COURSE, name="edit_class_course"),
    path('Hod/Class/Course/Update', HOD_views.UPDATE_CLASS_COURSE, name="update_class_course"),
    path('Hod/Class/Course/Delete/<str:id>', HOD_views.DELETE_CLASS_COURSE, name="delete_class_course"),

    # HOD to Staff Notification
    path('Hod/Staff/Send_Notification', HOD_views.SEND_NOTIFICATION_STAFF, name="send_notification_staff"),
    path('Hod/Staff/Save_Notification', HOD_views.SAVE_NOTIFICATION_STAFF, name="save_notification_staff"),
    path('Hod/Staff/View_Notification', HOD_views.VIEW_NOTIFICATION_STAFF, name="view_notification_staff"),
    path('Hod/Staff/Resend_Notification/<str:id>', HOD_views.RESEND_NOTIFICATION_STAFF, name="resend_notification_staff"),

    # HOD to Student Notification
    path('Hod/Student/Send_Notification', HOD_views.SEND_NOTIFICATION_STUDENT, name="send_notification_student"),
    path('Hod/Student/Save_Notification', HOD_views.SAVE_NOTIFICATION_STUDENT,name="save_notification_student"),
    path('Hod/Student/View_Notification', HOD_views.VIEW_NOTIFICATION_STUDENT, name="view_notification_student"),
    path('Hod/Student/Resend_Notification/<str:id>', HOD_views.RESEND_NOTIFICATION_STUDENT,name="resend_notification_student"),

#  HOD Result
    path('Hod/View/Result', HOD_views.HOD_VIEW_RESULT, name="hod_view_result"),
    path('Hod/View/Result/Student/<str:id>', HOD_views.HOD_VIEW_RESULT_STUDENT, name="hod_view_result_student"),



# staff Urls
    path('Staff/Home', staff_views.HOME, name="staff_home"),

    # Staff Notification
    path('Staff/Notification', staff_views.NOTIFICATION, name="staff_notification"),
    path('Staff/Mark_as_done/<str:status>', staff_views.STAFF_NOTIFY_MARK_AS_DONE, name="staff_notify_mark_as_done"),
    path('Staff/Inbox/<str:id>', staff_views.STAFF_INBOX, name="staff_inbox"),

    # Add Result BY Staff
    path('Staff/Result/Add', staff_views.STAFF_ADD_RESULT, name="staff_add_result"),
    path('Staff/Result/Save', staff_views.STAFF_SAVE_RESULT, name="staff_save_result"),

    # view Results
    path('Staff/View/Result', staff_views.STAFF_VIEW_RESULT, name="staff_view_result"),
    path('Staff/View/Result/Chart', staff_views.STAFF_VIEW_RESULT_CHART, name="staff_view_result_chart"),
    path('Staff/View/Result/Student/<str:id>/<str:cid>', staff_views.STAFF_VIEW_RESULT_STUDENT, name="staff_view_result_student"),
    path('Staff/Edit/Result/Student/<str:id>/<str:date>/<str:subid>', staff_views.STAFF_EDIT_RESULT_STUDENT, name="staff_edit_result_student"),
    path('Staff/Update/Result/Student', staff_views.STAFF_UPDATE_RESULT_STUDENT, name="staff_update_result_student"),
    path('Staff/Delete/Result/Student/<str:id>', staff_views.STAFF_DELETE_RESULT_STUDENT, name="staff_delete_result_student"),
    # path('Hod/Class/Course/Delete/<str:id>', HOD_views.DELETE_CLASS_COURSE, name="delete_class_course"),

# Students Urls
    path('Students/Home', student_views.HOME, name="student_home"),

     # Students Notification
    path('Students/Notification', student_views.NOTIFICATION, name="student_notification"),
    path('Students/Mark_as_done/<str:status>', student_views.STUDENT_NOTIFY_MARK_AS_DONE,name="student_notify_mark_as_done"),
    path('Students/Inbox/<str:id>', student_views.STUDENT_INBOX, name="student_inbox"),

    # view Results
    path('Students/View/Result', student_views.STUDENT_VIEW_RESULT, name="student_view_result"),


]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
