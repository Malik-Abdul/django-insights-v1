from  django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Home Page")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("About Page")
    return render(request, 'about.html')

