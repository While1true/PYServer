from django.db import models

# Create your models here.
class Category(models.Model):
    id=models.IntegerField(primary_key=True)
    category=models.CharField(max_length=50)
    addtime=models.DateField(auto_now=True)

    def __str__(self):
        return self.category


class Bug(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    category=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    issue=models.CharField(max_length=5000)
    time=models.DateField(auto_now=True)
    state=models.IntegerField(default=0)
    def __str__(self):
        return self.category
