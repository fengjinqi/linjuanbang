import time

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_GET,require_http_methods
# Create your views here.

import top.api
from apps.taobao.models import Banner,Carteary
from apps.utils.taobao import getTaoSettings
from datetime import datetime


@require_GET
def getTaoBanners(request):
    """
    获取banner
    :param request:
    :return:
    """
    obj = Banner.objects.values('pid','img','title','url','start_time','end_time','add_time').filter(end_time__gte=datetime.now())
    results = []
    for item in obj:
        jsonItem = {}
        jsonItem['pid']=item['pid']
        jsonItem['img']=item['img']
        jsonItem['title']=item['title']
        jsonItem['url']=item['url']
        jsonItem['start_time']=item['start_time']
        jsonItem['end_time']=item['end_time']
        results.append(jsonItem)
    return JsonResponse(results,safe=False)


@require_GET
def getCategory(request):
    """
    分类
    :param request:
    :return:
    """
    obj = Carteary.objects.values('comprehensive','shoe','mother','ladies','makeup','food','furnishing','mens','sports','digita','underwear').filter(active=True)
    results = []
    for item in obj:
        jsonItem = {}
        jsonItem['comprehensive']=item['comprehensive']
        jsonItem['shoe']=item['shoe']
        jsonItem['mother']=item['mother']
        jsonItem['ladies']=item['ladies']
        jsonItem['makeup']=item['makeup']
        jsonItem['food']=item['food']
        jsonItem['furnishing']=item['furnishing']
        jsonItem['mens']=item['mens']
        jsonItem['sports']=item['sports']
        jsonItem['digita']=item['digita']
        jsonItem['underwear']=item['underwear']
        results.append(jsonItem)
    return JsonResponse(results,safe=False)


@require_GET
def getHome(request):
    obj = Carteary.objects.values('comprehensive').filter(active=True)
    req=top.api.TbkDgOptimusMaterialRequest('https://eco.taobao.com/router/rest')
    req.set_app_info(top.appinfo(getTaoSettings().get('appkey'),getTaoSettings().get('secret')))
    req.page_size = 20
    req.adzone_id = int(getTaoSettings().get('adzone_id'))
    req.page_no = request.GET.get('page',1)
    if request.GET.get('id',''):
        req.material_id = request.GET.get('id')
    else:
        req.material_id = obj[0]['comprehensive']
    results = None
    try:
        results = req.getResponse()
    except Exception as e:
        print(e)
        results = e
    return JsonResponse(results)


def getSearch(request):


        #req=top.api.TbkDgOptimusMaterialRequest('https://eco.taobao.com/router/rest')
    req=top.api.TbkDgMaterialOptionalRequest('https://eco.taobao.com/router/rest')
    req.set_app_info(top.appinfo(getTaoSettings().get('appkey'),getTaoSettings().get('secret')))
    req.page_size=20
    req.adzone_id=int(getTaoSettings().get('adzone_id'))
    req.need_free_shipment = 'true'
    req.page_no = request.GET.get('page',1)
    req.material_id=6707
    req.q = request.GET.get('q','')
    req.has_coupon = 'true'
    results = None
    try:
        results= req.getResponse()
    except Exception as e:
        print(e)
        results = e

    return JsonResponse(results)
    #return render(request,'taobaoIndex.html',locals())