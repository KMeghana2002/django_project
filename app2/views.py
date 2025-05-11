from django.shortcuts import render

# Create your views here.
def arrivals(request):
    return render(request,'arrivals.html')
def blogs(request):
    return render(request,'blogs.html')
def reviews(request):
    return render(request,'reviews.html')
