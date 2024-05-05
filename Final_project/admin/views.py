from django.shortcuts import render,redirect
from customer.models import customer
from django.contrib import messages
from order.models import Order

# Create your views here.
def index(request):
    if 'admin_email' in request.session:
        return render(request, 'index_admin.html')
    else:
        return redirect('admin_login')

def admin_tutor(request):
    if 'admin_email' in request.session:
       return redirect('add_course')
    else:
        return redirect('admin_login')

def order_index(request):
    if 'admin_email' in request.session:
        ord_obj = Order.objects.select_related('cus_id','tutor_id','payment_method',).all()
        dict = {'d':ord_obj}
        return render(request, 'Order_admin.html', dict)
    else:
        return redirect('admin_login')

def login(request):
    if 'admin_email' in request.session:
        return redirect('admin_login')
    else:
        msg = messages.get_messages(request)
        context = {'msg':msg}
        return render(request, 'login_admin.html', context)
       

def logout(request):
        request.session.flush()
        return redirect('admin_login')

def login_admin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    admin_email = 'tutionportalfp@gmail.com'
    admin_pass = '1234'
    if email != admin_email:
        messages.success(request, "Your email is Wrong")
        return redirect('login')
    elif password != admin_pass:
        messages.success(request, "Your email is Wrong")
        return redirect('login')
    elif email == admin_email and password == admin_pass:
        request.session['admin_email'] = email
        return redirect('admin')
    else:
        return redirect('login')


def admin_customer(request):
    if 'admin_email' in request.session:
        all_data = customer.objects.all()
        dict = {'d':all_data}
        return render(request, 'Cus_admin.html', dict)
    else:
        return redirect('admin_login')

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

def cus_delete(request, id):
    data = customer.objects.get(id=id)
    data.delete()
    return redirect('admin_customer')