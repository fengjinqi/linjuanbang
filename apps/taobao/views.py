import time

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

import top.api
from apps.utils.taobao import getTaoSettings


def getTaoHome(request):
    print(request.COOKIES)
    if request.is_ajax():
        req=top.api.TbkDgOptimusMaterialRequest('https://eco.taobao.com/router/rest')

        req.set_app_info(top.appinfo(getTaoSettings().get('appkey'),getTaoSettings().get('secret')))



        req.page_size=20
        req.adzone_id=getTaoSettings().get('adzone_id')
        req.page_no=1
        req.material_id=6708
        # req.device_value="xxx"
        # req.device_encrypt="MD5"
        # req.device_type="IMEI"
        #req.content_id=596771289892
        # req.content_source="xxx"
        # req.item_id=33243
        results = None
        try:
            results= req.getResponse()
        except Exception as e:
            print(e)
            results = e
        return JsonResponse(results)
    return render(request,'taobaoIndex.html',locals())