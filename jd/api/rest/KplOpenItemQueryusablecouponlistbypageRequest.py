from jd.api.base import RestApi

class KplOpenItemQueryusablecouponlistbypageRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.uid = None
			self.pageNum = None

		def getapiname(self):
			return 'jd.kpl.open.item.queryusablecouponlistbypage'






