from enum import unique

from django.db import models

# Create your models here.
class master(models.Model):
    id=models.IntegerField(primary_key=True)
    category=models.CharField(max_length=50)
    come=models.CharField(max_length=50)
    content=models.CharField(max_length=5000)
    timestr=models.CharField(max_length=50)
    fid=models.CharField(max_length=50)
    mid=models.CharField(max_length=50)
    datelong=models.CharField(max_length=50)
    hrefStr=models.CharField(max_length=50)
    href=models.CharField(max_length=200)
    imgs=models.CharField(max_length=2000)

    def __str__(self):
        return self.content

class Like(models.Model):
    like_id=models.IntegerField()
    like_date=models.DateField(auto_now=True)
    like_user=models.CharField(max_length=200)
