from jd.api.base import RestApi

class KplOpenConfigOauthSaveRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.code = None
			self.tgt = None
			self.appId = None
			self.callSource = None
			self.callTarget = None
			self.client = None
			self.clientIp = None

		def getapiname(self):
			return 'jd.kpl.open.config.oauth.save'






