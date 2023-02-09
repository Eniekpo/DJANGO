from django import forms
from . models import Client, SMOKER
from django.core.validators import RegexValidator

# EVERY LETTER TO LOWER CASE


class LowerCase(forms.CharField):
    def to_python(self, value):
        return value.lower()

# EVERY LETTER TO UPPER CASE


class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class ClientForm(forms.ModelForm):
    # VALIDATIONS
    firstname = forms.CharField(
        label='First Name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only letter is allowed !')],
        # required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )

    lastname = forms.CharField(
        label='Last Name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only letter is allowed !')],
        # required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    # Job code always in upper case
    job = Uppercase(
        label='Job Code', min_length=5, max_length=5,
        widget=forms.TextInput(attrs={
            'placeholder': 'Example: FR-22',
        }),
        required=True
    )

# Email always invlower case
    email = LowerCase(
        label='Email Address', min_length=10, max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$',
                                   message='Put a valid email address !')],
        # required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'})
    )
    # Method
    # age = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}))

    age = forms.CharField(
        label='Your Age', min_length=2, max_length=3,
        validators=[RegexValidator(r'^[0-9]+$',
                                   message='Only numbers is allowed !')],
        # required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your Age'})
    )

    experience = forms.BooleanField(label='I have experience', required=False,)

    message = forms.CharField(
        label='Message', min_length=5, max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Message', 'rows': 3})
    )

# METHOD 1 TO GENDER 
    # GENDER = [('M', 'Male'), ('F', 'Female')]
    # gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect(choices=GENDER))                          

    class Meta:
        model = Client
        exclude = ("created_at", "Situation")

        SALARY = (
            ("", "Salary Expectation (Month"),
            ("Between ($500 and $1000)", "Between ($500 and $1000)"),
            ("Between ($1000 and $5000)", "Between ($1000 and $5000)"),
            ("Between ($5000 and $10000)", "Between ($5000 and $10000)"),
            ("Between ($10000 and $20000)", "Between ($10000 and $20000)"),
        )

        # METHOD 2 TO GENDER
        GENDER = [('M', 'Male'), ('F', 'Female')]

        # OUTSIDE WIDGET
        widgets = {
            # Phone
            'phone': forms.TextInput(
                attrs={'style': 'font-size:18px',
                       'placeholder': 'Phone Number',
                       'data-mask': '(000) 000000 0000'
                       }
            ),

            # SALARY
            'salary': forms.Select(
                choices=SALARY,
                attrs={
            'class': 'form-control' # Bootstrap inside the forms.py
                       }
            ),

            'gender': forms.RadioSelect(choices=GENDER, attrs={'class': 'btn-check'}),
            'smoker': forms.RadioSelect(choices=SMOKER, attrs={'class': 'btn-check'}),
        }

