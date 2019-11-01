from jd.api.base import RestApi

class KplOpenShenzhouConfigGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.tgt = None
			self.appId = None
			self.client = None
			self.clientIp = None
			self.sequence = None

		def getapiname(self):
			return 'jd.kpl.open.shenzhou.config.get'






