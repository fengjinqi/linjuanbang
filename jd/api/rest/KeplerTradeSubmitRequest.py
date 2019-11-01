from jd.api.base import RestApi

class KeplerTradeSubmitRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.cartReq = None
			self.orderParam = None

		def getapiname(self):
			return 'jd.kepler.trade.submit'






