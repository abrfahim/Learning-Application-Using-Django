from django.shortcuts import render, HttpResponse, redirect
from course_app.models import Course, Video
from course_app.forms import RegistrationForm, LoginForm
from django.views import View
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView


# class based view

class SignUpView(FormView):
    template_name = 'course_app/signup.html'
    form_class = RegistrationForm
    success_url = '/login'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LogInView(FormView):
    template_name= 'course_app/login.html'
    form_class = LoginForm
    success_url = '/'
    
    def form_valid(self, form):
        login(self.request, form.cleaned_data)
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect('next_page')
        return super().form_valid(form)



"""
class SignUpView(View):
    def get(self, request):
        form = RegistrationForm()
        
        diction ={'form': form}
        return render(request, template_name='course_app/signup.html', context=diction)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if (user is not None):
                return redirect('course_app:login')
        diction ={'form': form}
        return render(request, template_name='course_app/signup.html', context=diction)

    

class LogInView(View):
    def get(self, request):
        form = LoginForm()
        diction = {'form': form}
        return render(request, template_name= 'course_app/login.html', context=diction)
    
    def post(self, request):
        form= LoginForm(request= request, data = request.POST)
        diction = {'form': form}
        if form.is_valid():
            return redirect('course_app:home')
        return render(request, template_name= 'course_app/login.html', context=diction)

"""   
    
def log_out(request):
    logout(request)
    return redirect('home')
    
    
