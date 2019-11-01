from jd.api.base import RestApi

class OrderJdOrderIDByThridOrderIDQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.thirdOrder = None

		def getapiname(self):
			return 'biz.order.jdOrderIDByThridOrderID.query'






