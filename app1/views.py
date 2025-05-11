from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def login_form(request):
    return render(request,'login_form.html')
def featured(request):
    return render(request,'featured.html')
