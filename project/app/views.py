from django.shortcuts import render,redirect,HttpResponse
def home(request):
    return render(request,'index.html')

# Create your views here.
