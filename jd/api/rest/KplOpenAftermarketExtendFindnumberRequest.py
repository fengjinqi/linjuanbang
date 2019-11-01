from jd.api.base import RestApi

class KplOpenAftermarketExtendFindnumberRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.client = None
			self.availableNumberReq = None

		def getapiname(self):
			return 'jd.kpl.open.aftermarket.extend.findnumber'






