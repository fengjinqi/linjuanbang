from jd.api.base import RestApi

class KplOpenTradeMasterGetaddressbyidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.client = None
			self.addressId = None

		def getapiname(self):
			return 'jd.kpl.open.trade.master.getaddressbyid'






