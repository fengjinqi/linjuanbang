from jd.api.base import RestApi

class UnionOpenCouponGiftStopRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.couponReq = None

		def getapiname(self):
			return 'jd.union.open.coupon.gift.stop'






