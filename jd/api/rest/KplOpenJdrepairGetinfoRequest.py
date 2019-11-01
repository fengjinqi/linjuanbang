from jd.api.base import RestApi

class KplOpenJdrepairGetinfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.state = None

		def getapiname(self):
			return 'jd.kpl.open.jdrepair.getinfo'






