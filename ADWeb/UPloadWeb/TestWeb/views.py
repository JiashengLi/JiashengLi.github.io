from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")

def toIndex(request):
    context = {}
    context['indexSource'] = 'wsnm,nmsl' #context变量即为HTML中需要引用的变量名
    return render(request, 'index.html', context)

def LinkgenIndexShow(request):
    context = {}
    context['linkGen'] = ""
    return render(request,'index.html',context)
def contact(request):
    context = {}
    context['linkGen'] = ""
    return render(request,'contact.html',context)
def course(request):
    context = {}
    context['linkGen'] = ""
    return render(request,'course.html',context)
def about(request):
    context = {}
    context['linkGen'] = ""
    return render(request,'about.html',context)
def testimonial(request):
    context = {}
    context['linkGen'] = ""
    return render(request,'testimonial.html',context)
