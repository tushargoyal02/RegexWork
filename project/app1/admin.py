from django.contrib import admin
from .models import Employee, Image

# Register your models here.


class ImageForm(admin.ModelAdmin): 
    list_display = ['id', 'model_name', 'model_pic']

    class Meta: 
        model = Image 


class Employee_detail(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email','phone', 'Aphone','College_name']

    class Meta:
        model = Employee    

admin.site.register(Employee, Employee_detail)

admin.site.register(Image, ImageForm)
        