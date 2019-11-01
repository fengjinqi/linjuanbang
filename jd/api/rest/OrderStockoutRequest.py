from jd.api.base import RestApi

class OrderStockoutRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.orderId = None
			self.completeDate = None
			self.operName = None

		def getapiname(self):
			return 'jingdong.orderStockout'






