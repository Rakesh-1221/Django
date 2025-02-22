from django.db import models

# Create your models here.
class list_item(models.Model):
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=300)
    class Meta:
        db_table='todo_list'