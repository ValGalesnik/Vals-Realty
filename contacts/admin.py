from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'phone', 'contact_date')
    list_display_links = ('id', 'name', 'phone')
    search_fields = ('name', 'email', 'listing', 'phone')
    list_per_page = 10


admin.site.register(Contact, ContactAdmin)
