from datetime import datetime

from django.db import models

# Create your models here.


class Tao(models.Model):
    appkey = models.CharField(max_length=100,verbose_name='appkey')
    secret = models.CharField(max_length=100,verbose_name='secret')
    adzone_id = models.CharField(max_length=60,verbose_name='adzone_id',default='')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.appkey

    class Meta:
        verbose_name = '配置'
        verbose_name_plural = verbose_name


class Carteary(models.Model):
    title = models.CharField(max_length=20,verbose_name='类型')
    active = models.BooleanField(default=False,verbose_name='是否启动')
    comprehensive = models.CharField(max_length=20,verbose_name='综合')
    shoe = models.CharField(max_length=20,verbose_name='鞋包配饰')
    mother = models.CharField(max_length=20,verbose_name='母婴')
    ladies = models.CharField(max_length=20,verbose_name='女装')
    makeup = models.CharField(max_length=20,verbose_name='美妆个护')
    food = models.CharField(max_length=20,verbose_name='食品')
    furnishing = models.CharField(max_length=20,verbose_name='家居家装')
    mens = models.CharField(max_length=20,verbose_name='男装')
    sports = models.CharField(max_length=20,verbose_name='运动户外')
    digita = models.CharField(max_length=20,verbose_name='数码家电')
    underwear = models.CharField(max_length=20,verbose_name='内衣')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=200,verbose_name='活动名称')
    url = models.TextField(verbose_name='跳转地址')
    img = models.URLField(verbose_name='图片地址',default='')
    start_time = models.DateField(default=datetime.now,verbose_name='活动开始时间')
    end_time = models.DateField(default=datetime.now,verbose_name='活动结束时间')
    pid = models.CharField(max_length=100,verbose_name='活动id')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = verbose_name