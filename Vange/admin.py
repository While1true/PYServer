from django.contrib import admin
from Vange.models import Bug,Publisher,Category
# Register your models here.

class MasterAdmin(admin.ModelAdmin):
    list_display = ('category','issue','publisher','time')

admin.site.register(Bug,admin_class=MasterAdmin)
admin.site.register([Publisher,Category])
# admin.site.register(Publisher,MasterAdmin)
# admin.site.register(Category,MasterAdmin)
