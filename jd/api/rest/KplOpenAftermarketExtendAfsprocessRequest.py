from jd.api.base import RestApi

class KplOpenAftermarketExtendAfsprocessRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.afsServiceId = None

		def getapiname(self):
			return 'jd.kpl.open.aftermarket.extend.afsprocess'






