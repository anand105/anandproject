from django.contrib import admin
from testapp.models import student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['rollnum','name','dob','marks','email','phonenumber','address']
admin.site.register(student,StudentAdmin)
