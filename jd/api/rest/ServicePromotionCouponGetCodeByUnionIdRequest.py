from jd.api.base import RestApi

class ServicePromotionCouponGetCodeByUnionIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.couponUrl = None
			self.materialIds = None
			self.unionId = None
			self.positionId = None
			self.pid = None

		def getapiname(self):
			return 'jingdong.service.promotion.coupon.getCodeByUnionId'






