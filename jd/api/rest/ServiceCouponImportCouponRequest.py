from jd.api.base import RestApi

class ServiceCouponImportCouponRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.unionId = None
			self.skuId = None
			self.couponLink = None

		def getapiname(self):
			return 'jingdong.service.coupon.importCoupon'






