from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path("",views.index,name='home'),
    path("loginpage",views.loginpage,name='loginpage'),
    path("registerPage",views.registerPage,name='registerPage'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("logoutuser",views.logoutuser,name="logoutuser"),
    path("resource",views.resource,name="resource"),
    path("student_dashboard/<pk>",views.student_dashboard,name="student_dashboard"),
    path("student",views.student,name="student"),
    path("studentDetail/<str:pk>",views.studentDetail,name="studentDetail"),
    path("sectionpage",views.sectionpage,name="sectionpage"),
    path("availablelab",views.availablelab,name="availablelab"),
    path("resourcebook",views.resourcebook,name="resourcebook"),
    path("labpage",views.labpage,name="labpage"),
    path("resourcepage/",views.resourcepage,name="resourcepage"),
    path("student_dashboard/<pk>",views.student_dashboard,name="student_dashboard"),
    path("create_section",views.create_section,name="create_section"),
    path("delete_section/<pk>",views.delete_section,name="delete_section"),
    path("cancel_lab/<pk>",views.cancel_lab,name="cancel_lab"),
    path("booklab/<pk>",views.booklab,name="booklab"),
    path("create_student/<pk>",views.create_student,name="create_student"),
    path("delete_student/<pk>",views.delete_student,name="delete_student"),
    path("delete_resource/<pk>",views.delete_resource,name="delete_resource"),
]
