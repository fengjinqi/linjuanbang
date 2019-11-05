from datetime import datetime

from django.db import models

# Create your models here.


class Sesstings(models.Model):
    name = models.CharField(max_length=20,verbose_name='名字')
    type = models.BooleanField(default=True,verbose_name='是否开启')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '配置'
        verbose_name_plural = verbose_name