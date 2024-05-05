from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import customer,Tutor


def admin_customer(request):
    all_data = customer.objects.all()
    dict = {'d':all_data}
    return render(request, 'Cus_admin.html', dict)

def home(request):
    name = Tutor.objects.all()
    dict = {'d':name}
    return render(request, 'index.html',dict)

def edit_tutor(request, id):
    data  = Tutor.objects.get(id=id)
    
    d = {'data':data}
    
    return render(request, 'edit_tutor.html', d)




def delete_tutor(request, id):
    data = Tutor.objects.get(id=id)
    data.delete()
    return redirect('add_course')


def cus_delete(request, id):
    data = customer.objects.get(id=id)
    data.delete()
    return redirect('admin_customer')

def cus_edit(request, id):
    cus_data = customer.objects.get(id=id)
    dict = {'d':cus_data}

    return render(request, 'cus_edit.html', dict)

def edit_cust(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    password = request.POST.get('Password')

    cus_obj = customer.objects.get(id=id)
    cus_obj.name = name
    cus_obj.email = email
    cus_obj.Phone = phone
    cus_obj.dob = dob
    cus_obj.password = password
    
    cus_obj.save()
    return redirect('admin_customer')




def admin_cus(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    password = request.POST.get('Password')

    cus_obj = customer()
    cus_obj.name = name
    cus_obj.email = email
    cus_obj.Phone = phone
    cus_obj.dob = dob
    cus_obj.password = password
    
    cus_obj.save()
    return redirect('admin_customer')

def admin(request):
    return render(request, 'index_admin.html')

def admin_tutor(request):
    return redirect('add_course')

def register(request):
    return render(request, 'register.html')
def add_tutor(request):
    all_obj = Tutor.objects.all()
    dict = {'d':all_obj}
    return render(request, 'tables-basic.html', dict)

def admin_add_tutor(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    grade = request.POST.get('grade')
    subject = request.POST.get('subject')
    timings = request.POST.get('timings')
    fee = request.POST.get('fee')
    desc = request.POST.get('desc')
    tutor_obj = Tutor()
    tutor_obj.name = name
    tutor_obj.email = email
    tutor_obj.Phone = phone
    tutor_obj.dob = dob
    tutor_obj.grade = grade
    tutor_obj.subject = subject
    tutor_obj.timings = timings
    tutor_obj.fee = fee
    tutor_obj.desc = desc
    tutor_obj.save()
    return redirect('add_course')

def login(request):
    return render(request, 'login.html')

def reg_cus(request):

    name = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm-password')
    dob = request.POST.get('dob')
    cus_obj = customer()
    cus_obj.name = name
    cus_obj.email = email
    cus_obj.Phone = phone
    cus_obj.password = password
    cus_obj.dob = dob
    cus_obj.save()

    return redirect('home')

def tutor_edit(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    grade = request.POST.get('grade')
    subject = request.POST.get('subject')
    timings = request.POST.get('timings')
    fee = request.POST.get('fee')
    desc = request.POST.get('desc')
    
    tutor_obj = Tutor.objects.get(id=id)
    
    tutor_obj.name = name
    tutor_obj.email = email
    tutor_obj.Phone = phone
    tutor_obj.dob = dob
    tutor_obj.grade = grade
    tutor_obj.subject = subject
    tutor_obj.timings = timings
    tutor_obj.fee = fee
    tutor_obj.desc = desc
    tutor_obj.save()
    return redirect('add_course')



