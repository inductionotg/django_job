from django.shortcuts import render
from testApp.models import *


# Create your views here.
def index(request):
    return render(request, 'testApp/index.html')


def hydjobs11(request):
    jobs_list = hydjobs.objects.order_by('date')
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testApp/hyd.html', context=my_dict)


def ban1(request):
    jobs_list3 = ban.objects.order_by('date')
    my_dict3 = {'jobs_list3': jobs_list3}
    return render(request, 'testApp/bang.html',context=my_dict3)


def chennai1(request):
    jobs_list1 = chennai.objects.all()
    my_dict = {'jobs_list1': jobs_list1}
    return render(request, 'testApp/chennai.html', context=my_dict)


def dela(request):
    jobs_list2 = delhi.objects.all()
    my_dict1 = {'jobs_list2': jobs_list2}
    return render(request, 'testApp/del.html', context=my_dict1)
