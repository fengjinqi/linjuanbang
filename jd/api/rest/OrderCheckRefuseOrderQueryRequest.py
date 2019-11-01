from jd.api.base import RestApi

class OrderCheckRefuseOrderQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.date = None
			self.page = None

		def getapiname(self):
			return 'biz.order.checkRefuseOrder.query'






