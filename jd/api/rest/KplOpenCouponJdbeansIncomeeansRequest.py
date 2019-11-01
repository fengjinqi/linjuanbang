from jd.api.base import RestApi

class KplOpenCouponJdbeansIncomeeansRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.clientIp = None
			self.amount = None
			self.businessId = None
			self.activityId = None
			self.token = None

		def getapiname(self):
			return 'jd.kpl.open.coupon.jdbeans.incomeeans'






