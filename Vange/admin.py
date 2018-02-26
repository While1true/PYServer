from django.contrib import admin
from Vange.models import Bug
# Register your models here.

class MasterAdmin(admin.ModelAdmin):
    list_display = ('category','issue','publisher','time')

admin.site.register(Bug,MasterAdmin)
