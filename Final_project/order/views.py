from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import Order
import random
from tutor.models import Tutor
from .models import payment_method
from customer.models import customer
from django.contrib import messages
# Create your views here.

def payment_index(request):
    return render(request, 'payment.html')

def payment_insert(request):
    name = request.POST.get('name')
    payment = payment_method()
    payment.payment_method = name
    payment.save()
    return redirect('payment')

def index(request,id):
    payment_obj = payment_method.objects.all()
    tutor_obj = Tutor.objects.get(id=id)
    # user_name = 'user_id' in request.session
    # discount = random.choices('1234567890',k=2)
    discount = ''.join(random.sample('1234567890', k=2))
    discount = int(discount)
    # int = int(tutor_obj.fee)
    fee = int(tutor_obj.fee)
    total = fee - discount
    msg = messages.get_messages(request)

    context = {'d':tutor_obj, 'dis':discount, 'total':total, 'payment':payment_obj, 'msg':msg}
    # return HttpResponse(discount)
    

    return render(request, 'order.html', context)


def insert(request):
    name = request.POST.get('name')
    payment_mth = request.POST.get('payment_method')
    tutor = request.POST.get('tutor')
    search = customer.objects.filter(name=name)
    dis = request.POST.get('dis')
    if not all([name, payment_mth,tutor, dis]):
        messages.success(request,"All Feilds are required!")
        return HttpResponseRedirect(f'{tutor}')
    elif not search:
        messages.success(request,"Customer Not Found, Please Enter a Valid Customer name")
        return HttpResponseRedirect(f'{tutor}')

    else:
        cus_obj  = customer.objects.get(name=name)
        tutor_obj = Tutor.objects.get(id=tutor)
        payment = payment_method.objects.get(id=payment_mth)
        order_obj = Order()
        order_obj.tutor_id = tutor_obj
        order_obj.cus_id = cus_obj
        order_obj.payment_method  = payment
        order_obj.discount = dis
        order_obj.save()
        return redirect('root')
    
    