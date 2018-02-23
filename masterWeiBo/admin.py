from django.contrib import admin
from masterWeiBo.models import master
# Register your models here.

class MasterAdmin(admin.ModelAdmin):
    list_display = ('category','content','timestr')

admin.site.register(master,MasterAdmin)
