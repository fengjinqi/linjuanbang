from django.shortcuts import render

# Create your views here.
import os
from configparser import ConfigParser
# BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
# print(BASE_DIR)
import top.api
# conf = ConfigParser()
# conf.read(BASE_DIR)

def getTaoHome(request):

    # req=top.api.TbkDgOptimusMaterialRequest('https://eco.taobao.com/router/rest')
    # req.set_app_info(top.appinfo(conf.get('taobao','appkey'),conf.get('taobao','secret')))
    #
    # req.page_size=20
    # req.adzone_id=109594100407
    # req.page_no=1
    # req.material_id=6708
    # req.device_value="xxx"
    # req.device_encrypt="MD5"
    # req.device_type="IMEI"
    # # req.content_id=323
    # # req.content_source="xxx"
    # # req.item_id=33243
    # try:
    #     resp= req.getResponse()
    #     print(resp)
    # except Exception as e:
    #     print(e)
    return render(request,'taobaoIndex.html')