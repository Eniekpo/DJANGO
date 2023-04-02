from django.shortcuts import redirect, render
from .forms import CandidateForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'djforms/index.html')

def forms(request):
    form = CandidateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Registration Successful!")
        return redirect('forms')
    
    context = {
        "form": form
    }
    return render(request, 'djforms/forms.html', context)
