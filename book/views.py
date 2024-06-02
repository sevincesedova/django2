from django.shortcuts import render
from .models import books

# Create your views here.
def home(request):
    bookk=books.objects.all()
    return render(request,'index.html', {"bookk": bookk})

def about__view(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')