import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','job.settings')
import django
django.setup()
from testApp.models import *
from faker import Faker
from random import *
fake=Faker()
def phoneNumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return  int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Teamlead','Backend','SDE-1','LeadUI'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','PHD'))
        faddress=fake.address()
        femail=fake.email()
        fphoneNumber=phoneNumbergen()
        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,
                                                     address=faddress,email=femail,phoneNumber=fphoneNumber)
        chennai_record = chennai.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,
                                                       eligibility=feligibility,
                                                       address=faddress, email=femail, phoneNumber=fphoneNumber)
        delhi_record = delhi.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,
                                                       eligibility=feligibility,
                                                       address=faddress, email=femail, phoneNumber=fphoneNumber)
        ban_record = ban.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,
                                                   eligibility=feligibility,
                                                   address=faddress, email=femail, phoneNumber=fphoneNumber)
populate(50)
