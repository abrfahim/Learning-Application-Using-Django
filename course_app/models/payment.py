from django.db import models
from course_app.models import Course, UserCourse
from django.contrib.auth.models import User

class Payment(models.Model):
    order_id = models.CharField(max_length=100, null = False)
    payment_id = models.CharField(max_length=100)
    user_course = models.ForeignKey(UserCourse, null= True, blank=True, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    