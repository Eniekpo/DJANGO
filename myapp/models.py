from django.db import models
# Create your models here.
SITUATION = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Disapproved', 'Disapproved')
)

PERSONALITY = (
    ('', 'Select a Personality'),
    ('I am Outgoing', 'I am Outgoing'),
    ('I am Sociable', 'I am Sociable'),
    ('I am antisocial', 'I am antisocial'),
    ('I am discret', ' am discret'),
    ('I am serious', 'I am serious')
)

SMOKER = (
    ('Yes', 'Yes'),
    ('No', 'NO'),
)

class Client(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    experience = models.BooleanField(null=True, default=False)
    smoker = models.CharField(max_length=10, choices=SMOKER, default='')
    email = models.EmailField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')

    # Capitalize First and Last Name
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return str(self.firstname)
