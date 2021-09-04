from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created',)
    search_fields=["name"]


admin.site.register(Category, CategoryAdmin)
