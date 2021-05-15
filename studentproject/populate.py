import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentproject.settings')
django.setup()

from testapp.models import *
from faker import Faker
from random import *
faker=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        frollnum=faker.random_int(min=1,max=9999)
        fname=faker.name()
        fdob=faker.date()
        fmarks=faker.random_int(min=1,max=100)
        femail=faker.email()
        fphonenumber=phonenumbergen()
        faddress=faker.address()
        s_record=Student.objects.get_or_create(rollnum=frollnum,name=fname,dob=fdob,marks=fmarks,email=femail,phonenumber=fphonenumber,address=faddress)
populate(300)
