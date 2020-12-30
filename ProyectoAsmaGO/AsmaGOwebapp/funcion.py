from .models import Students
from django.db import models

ola = Students.objects.all()
print(ola)
