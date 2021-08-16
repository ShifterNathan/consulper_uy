from django.db import models


class Category(models.Model):
    name=models.CharField(primary_key=True, max_length=50)
    image=models.ImageField(upload_to='category_home')
    description=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Specialty(models.Model):
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    completed=models.DateField(auto_now_add=False, null=True, blank=True)
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to='specialty_home')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
    
    def __str__(self):
        return '%s de %s' % (self.category_id, self.title)
    
