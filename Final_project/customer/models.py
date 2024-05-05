from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length = 500)
    dob = models.CharField(max_length = 500)
    Phone = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    password = models.CharField(max_length=100)
    v_status = models.CharField(max_length=100)
    v_c = models.CharField(max_length=100)