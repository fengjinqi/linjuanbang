from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_GET

import jd


@require_GET
def getRush(request):
    """
    搜索
    :param request:
    :return:
    """
    n=jd.api.UnionOpenGoodsJingfenQueryRequest('https://router.jd.com/api')
    n.set_app_info(jd.appinfo())
    n.eliteId = 22
    n.pageIndex = 1
    n.pageSize = 20
    n.sortName = 'price'
    n.sort = 'desc'

    results = None
    try:
        results= n.getResponse()
    except Exception as e:
        print(e)
        results = e

    return JsonResponse(results)