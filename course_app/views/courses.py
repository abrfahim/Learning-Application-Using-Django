from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, redirect
from course_app.models import Course, Video, UserCourse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url= 'login'), name='dispatch')
class MyCourseList(ListView):
    template_name='course_app/mycourses.html'
    context_object_name = 'user_courses'
    
    def get_queryset(self):
        return UserCourse.objects.filter(user= self.request.user)


def coursePage(request,slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    next_lecture = 2
    preview_lecture = None
    
    if serial_number is None:
        serial_number = 1
    else:
        next_lecture = int(serial_number) + 1
        if len(videos) < next_lecture:
            next_lecture = None
        
        preview_lecture = int(serial_number) - 1
        
    
    video = Video.objects.get(serial_number=serial_number, course=course)

    if (video.is_preview is False):
        if (request.user.is_authenticated is False):
            return redirect ('course_app:login')
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user , course = course)
                error = 'You are already enrolled in this course'   
            except:
                return redirect ('course_app:checkout', slug = course.slug)
    
    
    diction = {'course':course,'video':video, 'videos':videos, 'next_lecture':next_lecture, 'preview_lecture':preview_lecture}
    return render(request, template_name= 'course_app/course_page.html', context= diction)



"""
@login_required(login_url= 'login')
def mycourses(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user=user)
    diction = {'user_courses': user_courses}
    return render(request, template_name='course_app/mycourses.html', context=diction)
"""