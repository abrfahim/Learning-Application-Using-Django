from django.shortcuts import render
from course_app.models import Course
from django.views.generic import ListView


class HomePage(ListView):
    template_name= 'course_app/homepage.html'
    queryset = Course.objects.filter()
    context_object_name = 'courses'
    # active = False



"""
def home(request):
    #retrive
    courses = Course.objects.all()
    print(courses)
    diction =  {'courses': courses}
    return render(request, template_name= 'course_app/homepage.html', context= diction)
"""
