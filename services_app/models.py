from django.db import models
from home_app.models import Category

class Services(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    completed=models.DateField(auto_now_add=False, null=True, blank=True, help_text="Fecha de completación de la obra")
    content=models.CharField(max_length=50, null=True, blank=True, help_text="Descripción de la obra")
    image=models.ImageField(upload_to='services_services')
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):
        return '%s de %s' % (self.category, self.title)
