from django.contrib import admin
from .models import Student, Course, Enrolled, Faculty, Offers, Teaches, Account, Library, Book, Borrow, StdentMob, \
    RoomDetails, Department, Take, Class, Outing, Hostel, FeesInf, PreReq, Material


class StudentAdmin(admin.ModelAdmin):
    list_display = ('regno', 'name', 'dob')
    list_filter = ('dob', 'regno')
    search_fields = ('regno',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('cid', 'cname')


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('fid', 'fname', 'dnum')


admin.site.site_title = 'VIT ADMIN'
admin.site.site_header = 'VIT ADMIN'
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrolled)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Offers)
admin.site.register(Teaches)
admin.site.register(Account)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(StdentMob)
admin.site.register(RoomDetails)
admin.site.register(Department)
admin.site.register(Take)
admin.site.register(Class)
admin.site.register(Outing)
admin.site.register(Hostel)
admin.site.register(FeesInf)
admin.site.register(PreReq)
admin.site.register(Material)

