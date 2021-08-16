from django.contrib import admin
from .models import Category, Specialty

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    search_fields=["name"]

class SpecialtyAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    search_fields=["title", "category_id"]
    list_filter=["category_id"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Specialty, SpecialtyAdmin)