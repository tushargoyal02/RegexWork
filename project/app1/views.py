from django.shortcuts import render, HttpResponse
from .models import Employee, Image
# Create your views here.

def home(request):
    Images = Image.objects.all()
    context ={
        'Images': Images,
    }

    #Images

    if request.method == 'POST':
        print('in post')
        first_name = request.POST['first_Name']
        last_name = request.POST['last_Name']
        Email =  request.POST['Email']
        phone = request.POST['Number']
        Aphone = request.POST['Anumber']
        College = request.POST['College'] 

        # Shell
        user = Employee()
        user.first_name = first_name
        user.last_name = last_name
        user.email = Email
        user.phone = phone
        user.Aphone = Aphone
        user.college_name = College
        
        user.save()
    else:
        print('in else')

    return render(request, 'home.html', context)




def base(request):
    return render(request, 'base.html')


def Employeedata(request):
    #Employee.objects.all()
    a = Employee.objects.all()
    b = Employee.objects.get(pk=1)
    print(a)
    print(b)

    context = {
        'data': a,
        'data1': b,
        'message': 'Welcome REGex',
    }


    return render(request, 'homee.html', context)
    #return HttpResponse(b)

#ngrok download -->> Googleng