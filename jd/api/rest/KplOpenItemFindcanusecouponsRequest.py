from jd.api.base import RestApi

class KplOpenItemFindcanusecouponsRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.uid = None
			self.cid = None
			self.sku = None

		def getapiname(self):
			return 'jd.kpl.open.item.findcanusecoupons'






