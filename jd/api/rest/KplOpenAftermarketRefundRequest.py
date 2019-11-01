from jd.api.base import RestApi

class KplOpenAftermarketRefundRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.afsRefundDetailDto = None
			self.client = None

		def getapiname(self):
			return 'jd.kpl.open.aftermarket.refund'






