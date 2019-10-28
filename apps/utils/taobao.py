from apps.taobao.models import Tao


def getTaoSettings():
    results = Tao.objects.values('appkey','secret','adzone_id').first()

    return results