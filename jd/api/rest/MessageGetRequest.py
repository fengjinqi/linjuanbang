from jd.api.base import RestApi

class MessageGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.type = None

		def getapiname(self):
			return 'biz.message.get'






