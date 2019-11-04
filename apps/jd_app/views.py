from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_GET

import jd
from apps.jd_app.models import Category, Banner
from apps.utils.jd import getJDSettings


def category(request):
    """
    导航
    :param request:
    :return:
    """
    data = Category.objects.values('pid','name','type').filter(type='1').order_by('-sort')
    squared  = Category.objects.values('pid','name','type').filter(type='2').order_by('sort')
    resulte = []
    obj = []
    for i in data:
       obj.append(i)
    resulte.append(obj)
    obj = []
    for i in squared:
        obj.append(i)
    resulte.append(obj)
    return JsonResponse(resulte,safe=False)


def get_banner(request):
    """
    banner
    :param request:
    :return:
    """
    obj = Banner.objects.values( 'img', 'title', 'url', 'start_time', 'end_time', 'add_time').filter(
        end_time__gte=datetime.now())
    resulte = []
    for i in obj:
        resulte.append(i)
    return JsonResponse(resulte,safe=False)


@require_GET
def getList(request):
    """
    jD
    :param request:
    :return:
    """
    #n=jd.api.UnionOpenGoodsQueryRequest('https://router.jd.com/api')
    n=jd.api.UnionOpenGoodsJingfenQueryRequest('https://router.jd.com/api')
    n.set_app_info(jd.appinfo(getJDSettings().get('appkey'),getJDSettings().get('secret')))
    # n.eliteId = 22
    # n.pageIndex = 1
    # n.pageSize = 20
    # n.sortName = 'price'
    # n.sort = 'desc'
    n.goodsReq = {
        'eliteId':request.GET.get('type'),
        'pageIndex':request.GET.get('page',1),
        'pageSize':20
    }
    results= n.getResponse()
    print(results)
    return JsonResponse(results)