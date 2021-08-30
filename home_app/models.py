from django.db import models


class Category(models.Model):
    name=models.CharField(primary_key=True, max_length=50)
    image=models.ImageField(upload_to='category_home')
    description=models.CharField(max_length=100, help_text="Texto que aparecerá en la sección inicial")
    content=models.TextField(max_length=500, default="Servicio", help_text="Texto que explicará el servicio en cuestión")
    created=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Services(models.Model):
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    completed=models.DateField(auto_now_add=False, null=True, blank=True, help_text="Fecha de completación de la obra")
    content=models.CharField(max_length=50, null=True, help_text="Descripción de la obra")
    image=models.ImageField(upload_to='services_home')
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):
        return '%s de %s' % (self.category_id, self.title)
    
