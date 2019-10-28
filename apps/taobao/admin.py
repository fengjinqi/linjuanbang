from django.contrib import admin

# Register your models here.
from  .models import Tao,Carteary


class TaoAdmin(admin.ModelAdmin):
    list_display = ['appkey','secret','adzone_id','add_time']


class CartearyAdmin(admin.ModelAdmin):
    list_display = ['title','active','add_time']


admin.site.register(Tao,TaoAdmin)
admin.site.register(Carteary,CartearyAdmin)