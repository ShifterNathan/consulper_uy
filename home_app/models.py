from django.db import models
from django.urls import  reverse

class Category(models.Model):
    name=models.CharField(primary_key=True, max_length=50)
    slug=models.SlugField(unique=True, blank=True, null=True)
    image=models.ImageField(upload_to='category_home')
    description=models.CharField(max_length=100, help_text="Texto que aparecerá en la sección inicial")
    content=models.TextField(max_length=500, default="Servicio", help_text="Texto que explicará el servicio en cuestión")
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services_by_category', args=[self.slug])
