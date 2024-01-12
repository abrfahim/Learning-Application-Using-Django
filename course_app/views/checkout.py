from django.shortcuts import render, HttpResponse, redirect
from course_app.models import Course, Video, UserCourse, CouponCode
from course_app.models import Payment
from sslcommerz_lib import SSLCOMMERZ 
from django.contrib.auth.decorators import login_required


# API Integrations
KEY_ID = 'thevi6552744e8167c'
KEY_SECRET = 'thevi6552744e8167c@ssl'

settings = { 'store_id': KEY_ID, 'store_pass': KEY_SECRET, 'issandbox': True }
sslcommez = SSLCOMMERZ(settings)


@login_required(login_url='/login')
def checkout(request,slug):
    course = Course.objects.get(slug = slug)
    user = request.user
    action = request.GET.get('action')
    couponcode = request.GET.get('couponcode')
    coupon_code_message = None;
    coupon = None
    payment = None
    error = None
    order = None
    amount = None
    
    if error is None:
        amount = int((course.price-(course.price * course.discount* 0.01)) * 100)
        
        if amount == 0:
            userCourse = UserCourse(user = user, course = course)
            userCourse.save()
            return redirect('/mycourses')
        
        
    if action == 'create_payment':
        print('Create order object')
        order = 'Order created'
        
        # Payment Integrations
        post_body = {}
        post_body['total_amount'] = (course.price -(course.price * course.discount * 0.01))
        post_body['currency'] = "BDT"
        post_body['tran_id'] = 'dkjfkjkfj'
        post_body['success_url'] = "your success url"
        post_body['fail_url'] = "your fail url"
        post_body['cancel_url'] = "your cancel url"
        post_body['emi_option'] = 0
        post_body['cus_name'] = "test"
        post_body['cus_email'] = "test@test.com"
        post_body['cus_phone'] = "01700000000"
        post_body['cus_add1'] = "customer address"
        post_body['cus_city'] = "Dhaka"
        post_body['cus_country'] = "Bangladesh"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1
        post_body['product_name'] = "Test"
        post_body['product_category'] = "Test Category"
        post_body['product_profile'] = "general"
        
        response = sslcommez.hash_validate_ipn(post_body)
        print(response)

    
    if couponcode:
        try:
            coupon = CouponCode.objects.get(course =  course, code = couponcode)
        except:
            coupon_code_message = 'Invalid coupon code'
    
    diction = {'course':course, 'order':order, 'coupon':coupon, 'coupon_code_message':coupon_code_message}
    return render(request, template_name= 'course_app/checkout.html', context= diction)