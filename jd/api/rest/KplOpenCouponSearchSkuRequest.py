from jd.api.base import RestApi

class KplOpenCouponSearchSkuRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.couponBatchId = None
			self.pageParam = None

		def getapiname(self):
			return 'jd.kpl.open.coupon.search.sku'






