from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.category.__str__()
class Publisher(models.Model):
    publisher = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.publisher.__str__()

class Bug(models.Model):
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    publisher=models.ForeignKey('Publisher',on_delete=models.CASCADE)
    title=models.CharField(max_length=100,default="")
    issue=models.TextField(max_length=5000)
    time=models.DateField(auto_now=True)
    state=models.IntegerField(default=0 ,choices=((0,"待解决"),(1,"已解决")))
    like=models.IntegerField(default=0,choices=((0,"未关注"),(1,"已关注")))
    def __str__(self):
        return self.category.__str__()


    # def __init__(self, *args, **kwargs):
    #     super(Bug, self).__init__(*args, **kwargs)
    #     self.category=models.CharField(max_length=50,choices=((x.que, x.disr) for x in Category.objects.all()))
