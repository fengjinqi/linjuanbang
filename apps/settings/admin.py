from django.contrib import admin

# Register your models here.
from apps.settings.models import Sesstings


class SesstingsAdmin(admin.ModelAdmin):
    list_display = ['name','type','add_time']


admin.site.register(Sesstings,SesstingsAdmin)