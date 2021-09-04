from django.contrib import admin
from .models import Services

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields=('created',)
    search_fields=["title", "category"]
    list_filter=["category"]

admin.site.register(Services, ServicesAdmin)