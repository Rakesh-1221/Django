from django.db import models

# Create your models here.
class registration(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=15)
    class Meta:
        db_table='register_table'

    def __str__(self):
        return self.username
