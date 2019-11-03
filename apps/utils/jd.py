from apps.jd_app.models import JD


def getJDSettings():
    results = JD.objects.values('appkey','secret').first()

    return results