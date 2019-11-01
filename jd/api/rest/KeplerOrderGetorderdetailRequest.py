from jd.api.base import RestApi

class KeplerOrderGetorderdetailRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.client = None

		def getapiname(self):
			return 'jd.kepler.order.getorderdetail'






