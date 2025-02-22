from django.db import models

# Create your models here.
class login_data(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    email=models.EmailField()
    class Meta:
        db_table = "login"

