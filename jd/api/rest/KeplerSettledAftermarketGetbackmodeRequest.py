from jd.api.base import RestApi

class KeplerSettledAftermarketGetbackmodeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.wareId = None
			self.backAddr = None
			self.client = None

		def getapiname(self):
			return 'jd.kepler.settled.aftermarket.getbackmode'






