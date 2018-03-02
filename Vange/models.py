from django.db import models

# Create your models here.
class MyManager(models.Manager):
    def get_by_natural_key(self,category,publisher):
        return self.get(category=category,publisher=publisher)

class Category(models.Model):
    category=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.category.__str__()
    def natural_key(self):
        return self.category
    class Meta:
        verbose_name = "项目列表"
        verbose_name_plural = "项目列表"

class Publisher(models.Model):
    publisher = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.publisher.__str__()
    def natural_key(self):
        return self.publisher
    class Meta:
        verbose_name = "测试人员"
        verbose_name_plural = "测试人员"

class Bug(models.Model):
    category=models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name="项目名称")
    publisher=models.ForeignKey('Publisher',on_delete=models.CASCADE,verbose_name="发布者")
    title=models.CharField(max_length=100,default="",verbose_name="概要说明")
    issue=models.TextField(max_length=5000,verbose_name="问题描述")
    time=models.DateField(auto_now=True,verbose_name="发布时间")
    state=models.IntegerField(default=0 ,choices=((0,"待解决"),(1,"已解决")),verbose_name="是否解决")
    like=models.IntegerField(default=0,choices=((0,"未关注"),(1,"已关注")),verbose_name="特别关注")
    def __str__(self):
        return self.category.__str__()+self.publisher.__str__()
    def natural_key(self):
        return (self.category.natural_key(),self.publisher.natural_key())

    class Meta:
        unique_together = (('publisher', 'category'),)
        verbose_name = "Bug列表"
        verbose_name_plural = "Bug列表"



    # def __init__(self, *args, **kwargs):
    #     super(Bug, self).__init__(*args, **kwargs)
    #     self.category=models.CharField(max_length=50,choices=((x.que, x.disr) for x in Category.objects.all()))
