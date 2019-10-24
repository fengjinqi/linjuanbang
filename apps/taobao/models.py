from datetime import datetime

from django.db import models

# Create your models here.


class Tao(models.Model):
    appkey = models.CharField(max_length=100,verbose_name='appkey')
    secret = models.CharField(max_length=100,verbose_name='secret')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.appkey

    class Meta:
        verbose_name = '配置'
        verbose_name_plural = verbose_name