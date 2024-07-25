from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse('<h1> Hello World </h1>')
    return render(request , 'myapp/home.html')

def about(request):
    # return HttpResponse('<h2> I am about page </h2>')
    about = "We are building an app"
    return render(request , 'myapp/about.html', {'about': about})

def contact(request):
    # return HttpResponse('<h2> I am contact page </h2>')
    return render(request , 'myapp/contact.html')