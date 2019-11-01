from jd.api.base import RestApi

class KplOpenYaoOrdersyncUpdatestateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.orderId = None
			self.deliverInfo = None

		def getapiname(self):
			return 'jd.kpl.open.yao.ordersync.updatestate'






