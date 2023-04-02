from django import forms
from django.core.validators import RegexValidator
from .models import Candidate

class CandidateForm(forms.ModelForm):

    # VALIDATIONS
    firstname = forms.CharField(
        min_length=3, max_length=50, label='First Name', 
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$', message='Only letter is allowed !')],
                                   required=True,
        widget=forms.TextInput(
         attrs={'placeholder': 'First Name'})
        )
        
    lastname = forms.CharField(
        min_length=3, max_length=50, label='Last Name', 
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$', message='Only letter is allowed !')],
                                   required=True,
        widget=forms.TextInput(
         attrs={'placeholder': 'Last Name'})
        )
    
    email = forms.CharField(
        min_length=10, max_length=50, label='Email Address', 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
                                   message='Put a Valid Email Address !!')],
                                   required=True,
        widget=forms.TextInput(
         attrs={'placeholder': 'Email'})
        )
    
    # Method 1
    # age = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}))

    # Method 2 

    age = forms.CharField(
        min_length=2, 
        max_length=3, 
        label='Your Age', 
        validators=[RegexValidator(r'^[0-9]*$', 
                                   message='Only Numbers is Allowed!')],
                                   required=True,
        widget=forms.TextInput(
         attrs={'placeholder': 'Age'})
        )
    
    message = forms.CharField(
        min_length=10, 
        max_length=1000, 
        label='Your Bio', 
         required=False,
        widget=forms.Textarea(
         attrs={'placeholder': 'About Yourself', 'rows':4}
         ),
        )

    class Meta:
        model = Candidate
        fields = '__all__'
       # exclude = ["firstname", "lastname", "age", "email", "message"]
       # fields = ["firstname", "lastname", "age", "email", "message"]