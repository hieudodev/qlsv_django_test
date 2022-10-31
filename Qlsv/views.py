from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import sinhvien
from django.urls import reverse
# Create your views here.

# def showStu(request):
#     stu = 'Nguyen Van Hieu'
#     return HttpResponse(stu)

# def index(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

# def index(request) :
#     stus = sinhvien.objects.all().values()
#     output = ""
#     for x in stus :
#         output += x["firstname"]
#     return HttpResponse(output)

def index(request):
     stus = sinhvien.objects.all().values()
     template = loader.get_template('index.html')
     context = {
        'stus' : stus,
     }
     return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    stu = sinhvien(firstname = x, lastname = y)
    stu.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    stu = sinhvien.objects.get(id = id )
    stu.delete()
    return HttpResponseRedirect(reverse('index'))
def update(request, id):
  mymember = sinhvien.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = sinhvien.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))    