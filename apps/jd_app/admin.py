from django.contrib import admin

# Register your models here.
from apps.jd_app.models import JD


class JDAdmin(admin.ModelAdmin):
    list_display = ['appkey','secret','add_time']


admin.site.register(JD,JDAdmin)