from jd.api.base import RestApi

class KeplerTradeGetstockRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skus = None
			self.area = None
			self.category = None
			self.venderId = None

		def getapiname(self):
			return 'jd.kepler.trade.getstock'






