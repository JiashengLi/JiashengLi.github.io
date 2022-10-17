from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")

def linkgenWeb(request):
    context = {}
    context['linkGen'] = ""
    return render(request,'LinkGenHomepage.html',context)
def linkgenWebIndex(request):
    context = {}
    context['linkGen'] = ""
    return render(request,'index.html',context)
def LinkgenProductShow(request):
    context = {}
    context['linkGen'] = ""
    return render(request,'product-show.html',context)