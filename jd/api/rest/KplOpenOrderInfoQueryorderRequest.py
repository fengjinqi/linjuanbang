from jd.api.base import RestApi

class KplOpenOrderInfoQueryorderRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.var1 = None

		def getapiname(self):
			return 'jd.kpl.open.order.info.queryorder'






