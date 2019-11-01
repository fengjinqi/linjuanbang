from jd.api.base import RestApi

class KplOpenClientGetunplRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.jda = None
			self.url = None
			self.siteId = None
			self.ip = None
			self.ua = None

		def getapiname(self):
			return 'jd.kpl.open.client.getunpl'






