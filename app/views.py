from django.shortcuts import render, HttpResponse

from datetime import datetime
from app.models import Home
def home(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        rating=request.POST.get('rating')
        other=request.POST.get('other')
        home=Home(name=name, email=email, rating=rating, other=other, date=datetime.now())
        home.save()
    return render(request, 'gym.html')
def about(request):
    return HttpResponse("this is about page")
def service(request):
    return HttpResponse("this is service page")

