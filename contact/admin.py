from django.contrib import admin
from .models import Contact




class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = (
        'subject', 'email', 'name',
    )


admin.site.register(Contact, ContactAdmin)