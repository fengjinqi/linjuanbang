from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_GET

import jd
from apps.utils.jd import getJDSettings


@require_GET
def getRush(request):
    """
    搜索
    :param request:
    :return:
    """
    n=jd.api.UnionOpenGoodsQueryRequest('https://router.jd.com/api')
    #n=jd.api.UnionOpenGoodsJingfenQueryRequest('https://router.jd.com/api')
    print(getJDSettings().get('appkey'))
    n.set_app_info(jd.appinfo('dd0e33fbd25eaab95f50cfebc72d8925','51400be7286e49f4aae8c37b64a7e443'))
    # n.eliteId = 22
    # n.pageIndex = 1
    # n.pageSize = 20
    # n.sortName = 'price'
    # n.sort = 'desc'
    n.goodsReq = {
        'eliteId':22
    }
    n.goodsReqDTO={
        'keyword':'手机'
    }
    results = None
    #try:
    results= n.getResponse()
    #except Exception as e:
     #   print(e)
     #   results = e

    return JsonResponse(results)