from django.db import models

# Create your models here.
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    curso=models.CharField(max_length=255)
    colegio=models.CharField(max_length=255)
    velocidad=models.CharField(max_length=255)
    resistencia=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    objects=models.Manager()