from datetime import datetime

from django.db import models

# Create your models here.


class JD(models.Model):
    appkey = models.CharField(max_length=100,verbose_name='appkey')
    secret = models.CharField(max_length=100,verbose_name='secret')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.appkey

    class Meta:
        verbose_name = '配置'
        verbose_name_plural = verbose_name

"""

1-好券商品,
2-超级大卖场,
10-9.9专区,
22-热销爆品,
24-数码家电,
25-超市,
26-母婴玩具,
27-家具日用,
28-美妆穿搭,
29-医药保健,
30-图书文具,
31-今日必推,
32-王牌好货
"""


class Category(models.Model):
    CHOOSE = (
        ('1','导航'),
        ('2','九宫格'),
    )
    pid = models.CharField(max_length=10,verbose_name='分类id')
    name = models.CharField(max_length=20,verbose_name='分类名')
    sort = models.IntegerField(verbose_name='排序',default=0)
    type = models.CharField(max_length=10,choices=CHOOSE,verbose_name='显示',default='1')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name='活动名称')
    url = models.TextField(verbose_name='跳转地址')
    img = models.URLField(verbose_name='图片地址',default='')
    start_time = models.DateField(default=datetime.now,verbose_name='活动开始时间')
    end_time = models.DateField(default=datetime.now,verbose_name='活动结束时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = verbose_name