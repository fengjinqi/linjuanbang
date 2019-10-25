from apps.taobao.models import Tao


def getTaoSettings():
    results = Tao.objects.values('appkey','secret').first()

    return results