from django.urls import path
from course_app.views import SignUpView, coursePage, LogInView, log_out, checkout, MyCourseList
app_name = 'course_app'

urlpatterns = [
    path('course/<str:slug>', coursePage, name = 'coursepage'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LogInView.as_view(), name='login'),
    path('logout', log_out, name='logout'),
    path('check-out/<str:slug>', checkout, name = 'checkout'),
    path('mycourses/', MyCourseList.as_view(), name='mycourses'),
]
