from django import template
import math
from course_app.models import UserCourse, Course


register = template.Library()


@register.simple_tag
def cal_sellprice(price, discount):
    sell_price = price
    if discount is None or discount is 0:
        return sell_price
    else:
        sell_price = price - (price*discount*0.01)
        return math.ceil(sell_price)
    
@register.filter
def bdt(price):
    return f'\u09F3 {price}'


@register.simple_tag
def is_enrolled(request, course):
    user = None
    if not request.user.is_authenticated:
        return False
    user = request.user
    
    try:
        user_course = UserCourse.objects.get(user=user, course=course)
        return True
    except:
        return False
    