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

class WordCloud(models.Model):
    artical_id=models.IntegerField()
    user=models.CharField(max_length=200)
    url=models.CharField(max_length=1000)
    date=models.DateField(auto_now=True)
    pattern=models.CharField(max_length=1000,default="")

class WordPattern(models.Model):
    user=models.CharField(max_length=200,null=False)
    name=models.CharField(max_length=200,null=False)
    img=models.ImageField(upload_to="public/media")
