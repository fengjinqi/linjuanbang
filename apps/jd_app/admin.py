from django.contrib import admin

# Register your models here.
from apps.jd_app.models import JD,Category,Banner


class JDAdmin(admin.ModelAdmin):
    list_display = ['appkey','secret','add_time']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pid','name','type','add_time']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title','start_time','end_time','add_time']


admin.site.register(JD,JDAdmin)
admin.site.register(Banner,BannerAdmin)
admin.site.register(Category,CategoryAdmin)