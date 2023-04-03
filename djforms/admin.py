from django.contrib import admin
from .models import Candidate

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "age", "job", "phone", "email", "message"]
    search_fields = ["firstname", "lastname", "email", "phone"]
    list_per_page = 10

admin.site.register(Candidate, CandidateAdmin)  