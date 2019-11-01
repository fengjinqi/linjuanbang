from jd.api.base import RestApi

class KplOpenNosecretpaySavesignedRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.notify = None

		def getapiname(self):
			return 'jd.kpl.open.nosecretpay.savesigned'






