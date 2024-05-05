from django.db import models
from tutor.models import Tutor
from customer.models import customer

class payment_method(models.Model):
    payment_method = models.CharField(max_length = 400)

# Create your models here.
class Order(models.Model):
    cus_id = models.ForeignKey(customer, models.CASCADE)
    tutor_id = models.ForeignKey(Tutor, models.CASCADE)
    payment_method  = models.ForeignKey(payment_method, models.CASCADE)
    discount = models.CharField(max_length = 400)
