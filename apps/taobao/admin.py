from django.contrib import admin

# Register your models here.
from  .models import Tao


class TaoAdmin(admin.ModelAdmin):
    list_display = ['appkey','secret','add_time']

admin.site.register(Tao,TaoAdmin)