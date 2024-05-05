from django.shortcuts import render,redirect,HttpResponse
from . models import customer
from django.contrib import messages
import re
from datetime import datetime
import random
from django.core.signing import Signer
from django.core.mail import send_mail
from django.utils.html import format_html

# Create your views here.
def register(request):
    
    msg = messages.get_messages(request)
    dict = {'msg':msg}
    return render(request, 'register.html', dict)
    

def logout(request):
    request.session.flush()
    return redirect('login')



def reg_conf(request):
    return render(request,'reg_conf.html')

def reg_cus(request):

    name = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm-password')
    pattern = r"^[a-zA-Z0-9_.]+@(gmail|yahoo|outlook)\.(com|net|org)$"
    signer = Signer()
    search = customer.objects.filter(email=email)

    dob = request.POST.get('dob')
    if not all([name,email,phone,password, dob]):
        messages.success(request, "All feilds are Required!")
        return redirect('register')
    elif search:
        messages.success(request, "Email already exists!")
        return redirect('register')
    elif password != confirm_password:
        messages.success(request, "Please confirm your password!")
        return redirect('register')
    elif not re.match(pattern, email):
        messages.success(request, "Your email is not valid!")
        return redirect('register')
    elif len(phone) != 11:
        messages.success(request, "Phone must me 11 charecter")
    else:
        current_time = datetime.now().strftime("%H:%M:%S")
        h,m,s = map(int, current_time.split(':'))
        t_s = h*3600+m*60+s
        random_number = random.choices('1234567890',k=4)
        random_number = ''.join(random_number)
        t_s = str(t_s)
        v_c = t_s + random_number
        enc_val = signer.sign(v_c).split(":")[1]
        link = f"<p>Congratulations Mr. {name} ! For registering in our Tution Portal. To conform registration</p><a href='http://127.0.0.1:8000/customer/user/email_verification/"+enc_val+"'target='_blank'>please click this Activation link</a>"
        send_mail(f"Mr/Mrs.{name} Please confirm your registration - Tutuion Portal",enc_val,'tutionportfalfp@gmail.com',[email], html_message=link)


        cus_obj = customer()
        cus_obj.name = name
        cus_obj.email = email
        cus_obj.Phone = phone
        cus_obj.password = password
        cus_obj.dob = dob
        cus_obj.v_c = enc_val
        cus_obj.v_status = 0
        cus_obj.save()
        

    return redirect('reg_conf')


def login(request):
    google_data = request.session.get('social_auth_google-oauth2')
    #  or google_data
    if 'user_id' in request.session or google_data:
        return redirect('root')
    else:
        msg = messages.get_messages(request)
        dict = {'msg':msg}
        return render(request, 'login.html', dict)


def cus_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if not all([email, password]):
        messages.error(request, "All fields are required!")
        return redirect('login')
    
    search = customer.objects.filter(email=email)
    
    if not search:
        messages.error(request, "Email not found!")
        return redirect('login')
    
    log_data = customer.objects.get(email=email)
    
    if log_data.v_status == '0':
        messages.error(request, "You haven't completed email verification!")
        return redirect('login')
    
    if log_data.password != password:
        messages.error(request, "Wrong password!")
        return redirect('login')
    
    if log_data.password == password and log_data.v_status == '1':
        request.session['user_id'] = log_data.id
        request.session['user_name'] = log_data.name
        return redirect('root')
    
    return redirect('login')


def email_verify(request,id): 
    data = customer.objects.get(v_c = id)
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