from django.db import models

class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=18)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Capitalize F-Name and L-Name 
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return self.firstname
