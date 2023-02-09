from django.contrib import admin
from django.utils.html import format_html
from .models import Client
from .forms import ClientForm


class ClientAdmin(admin.ModelAdmin):
    radio_fields = {'smoker': admin.HORIZONTAL}
    form = ClientForm
    list_filter = ['Situation']
    list_display = ["firstname", "lastname", 'job', "age",
                    "email", "phone", "message", "created_at","status", "_"]
    search_fields = ["firstname", "lastname", "email", "Situation"]
    list_per_page = 10

    # Function to change the icon
    def _(self, obj):
        if obj.Situation == 'Approved':
            return True
        elif obj.Situation == 'Pending':
            return None
        else:
            return False
    _.boolean = True

    # Function to color the text


    def status(self, obj):
        if obj.Situation == 'Approved':
            color = '#28a745'
        elif obj.Situation == 'Pending':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.Situation))


    status.allow_tags = True

admin.site.register(Client, ClientAdmin)
