from django.shortcuts import render , HttpResponse

from home.models import Name

# Create your views here.

def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        contact = Name(fname=fname,lname=lname)
        contact.save()
    return render(request,"contact.html")