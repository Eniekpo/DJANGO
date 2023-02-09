from django.shortcuts import render
from . forms import ClientForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'myapp/index.html')

def login(request):
    return render(request, 'myapp/login.html')


def register(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "You Have Been Registered Successfully !")
        return HttpResponseRedirect('/register')
    context = {
        "form": form
    }

    return render(request, 'myapp/register.html', context)
