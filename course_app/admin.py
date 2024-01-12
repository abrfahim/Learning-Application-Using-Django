from django.contrib import admin
from course_app.models import Course, Tag, Learning, Prerequisite, Video,Payment, UserCourse, CouponCode
# Register your models here.
class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite
    
class VideoAdmin(admin.TabularInline):
    model = Video

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin]
    list_display = ['name', 'get_price', 'get_discount', 'active']
    list_filter = ('discount', 'active')
    
    def get_price(self,course):
        return f'{course.price} BDT'
    
    def get_discount(self,course):
        return f'{course.discount} %'
    
    get_discount.short_description = "Discount"
    get_price.short_description = "Price"
    
    

admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment)
admin.site.register(UserCourse)
admin.site.register(CouponCode)
