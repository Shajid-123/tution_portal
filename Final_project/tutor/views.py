from django.shortcuts import render,redirect,HttpResponse
from  .models import Tutor
from django.contrib import messages
import re
from datetime import datetime
import random
from django.core.signing import Signer
from django.core.mail import send_mail
from django.utils.html import format_html
from .forms import UploadFileForm
import pandas as pd

def details(request, id):
    tutor_obj = Tutor.objects.get(id=id)
    context = {'d':tutor_obj}
    return render(request, 'hd.html', context)

def search(request):
    search_val = request.POST.get('search')
    search_result  = Tutor.objects.filter(name__icontains = search_val)
    context = {'d':search_result}
    return render(request, 'search.html', context)

# Create your views here.
def add_tutor(request):
    if 'admin_email' in request.session:
        all_obj = Tutor.objects.all()
        msg = messages.get_messages(request)
        dict = {'d':all_obj, 'msg':msg}
        
        return render(request, 'tables-basic.html', dict)
    else:
        return redirect('admin_login')



def admin_add_tutor(request):
    img = request.FILES.get('images')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    grade = request.POST.get('grade')
    subject = request.POST.get('subject')
    timings = request.POST.get('timings')
    fee = request.POST.get('fee')
    desc = request.POST.get('desc')
    pattern = r"^[a-zA-Z0-9_.]+@(gmail|yahoo|outlook)\.(com|net|org)$"
    if not all([name,email,phone,img,dob]):
        messages.success(request, "All feilds are Required!")
        return redirect('add_course')
    
    elif not re.match(pattern, email):
        messages.success(request, "Your email is not valid!")
        return redirect('add_course')
    elif len(phone) != 11:
        messages.success(request, "Phone must me 11 charecter")
        return redirect('add_course')
    else:
        current_time = datetime.now().strftime("%H:%M:%S")
        h,m,s = map(int, current_time.split(':'))
        t_s = h*3600+m*60+s
        random_number = random.choices('1234567890',k=4)
        random_number = ''.join(random_number)
        t_s = str(t_s)
        v_c = t_s + random_number
        signer = Signer()
        enc_val = signer.sign(v_c).split(":")[1]
        link = f"<p>Congratulations Mr. {name} ! For registering in our Tution Portal. To conform registration</p><a href='http://127.0.0.1:8000/tutor/user/email_verification/"+enc_val+"'target='_blank'>please click this Activation link</a>"
        send_mail(f"Mr/Mrs.{name} Please confirm your registration - Tutuion Portal",enc_val,'tutionportfalfp@gmail.com',[email], html_message=link)
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
        tutor_obj.img = img
        tutor_obj.v_c = enc_val
        tutor_obj.v_status = 0
        tutor_obj.save()
        return redirect('reg_conf_tutor')

def edit_tutor(request, id):
    data  = Tutor.objects.get(id=id)
    
    d = {'data':data}
    
    return render(request, 'edit_tutor.html', d)

def tutor_edit(request):
    img = request.FILES.get('images')
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
    pattern = r"^[a-zA-Z0-9_.]+@(gmail|yahoo|outlook)\.(com|net|org)$"
    if not all([name,email,phone,img,dob]):
        messages.success(request, "All feilds are Required!")
        return redirect('tutor_edit')
    
    elif not re.match(pattern, email):
        messages.success(request, "Your email is not valid!")
        return redirect('tutor_edit')
    elif len(phone) != 11:
        messages.success(request, "Phone must me 11 charecter")
        return redirect('tutor_edit')
    else:
    
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
        tutor_obj.img = img
        
        tutor_obj.save()
        return redirect('add_course')


def delete_tutor(request, id):
    data = Tutor.objects.get(id=id)
    data.delete()
    return redirect('add_course')

def email_verify(request,id): 
    data = Tutor.objects.get(v_c = id)
    print(id)
    bool_val =  False
    if data.v_status == '0':
        data.v_status = 1
        data.save()
        bool_val = False
    else:
        bool_val = True
    bool_dic = {'d':bool_val}
    return render(request,'success.html',bool_dic)

def reg_conf(request):
    return redirect('reg_conf')
# {% url 'edit_tutor' i.id %}
# {% url 'delete_tutor' i.id %}