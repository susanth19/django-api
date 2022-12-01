from django.db import models

# Create your models here.
class Todo(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=100)
    # objects=models.DjongoManager(