from django.contrib import admin

# Register your models here.
from  .models import Tao,Carteary,Banner


class TaoAdmin(admin.ModelAdmin):
    list_display = ['appkey','secret','adzone_id','add_time']


class CartearyAdmin(admin.ModelAdmin):
    list_display = ['title','active','add_time']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['pid','title','img','start_time','end_time']

admin.site.register(Tao,TaoAdmin)
admin.site.register(Carteary,CartearyAdmin)
admin.site.register(Banner,BannerAdmin)