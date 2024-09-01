from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def details(request,slug):
    mymembers = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))
 
def testing(request):
    mymembers= Member.objects.all()
    template = loader.get_template('test.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context,request))