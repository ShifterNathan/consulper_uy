from django.contrib import admin
from .models import Category, Services

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created',)
    search_fields=["name"]

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields=('created',)
    search_fields=["title", "category_id"]
    list_filter=["category_id"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Services, ServicesAdmin)