from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('admin_panal/<phone>',views.admin_panal,name='admin_panal'),
    path('students_list/<host_id>',views.students_list,name='students_list'),
    path('student_delete/<student_id>',views.student_delete,name='student_delete'),
    path('view_edit_student/<student_id>',views.view_edit_student,name='view_edit_student'),
    path('add_student/<host_id>',views.add_student,name='add_student'),
    path('visitors_list/<student_id>',views.visitors_list,name='visitors_list'),
    path('view_edit_visitor/<visitor_id>',views.view_edit_visitor,name='view_edit_visitor'),
    path('add_visitors/<student_id>',views.add_visitors,name='add_visitors'),
    path('visitor_delete/<visitor_id>',views.visitor_delete,name='visitor_delete'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('add_hostel/<phone>',views.add_hostel,name='add_hostel'),
    path('search',views.search,name='search'),

]