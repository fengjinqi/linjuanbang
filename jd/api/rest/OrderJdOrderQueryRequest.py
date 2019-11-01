from jd.api.base import RestApi

class OrderJdOrderQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.jdOrderId = None

		def getapiname(self):
			return 'biz.order.jdOrder.query'






