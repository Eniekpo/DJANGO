from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'djforms/index.html')

def forms(request):
    return render(request, 'djforms/forms.html')
