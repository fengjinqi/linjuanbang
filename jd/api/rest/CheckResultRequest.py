from jd.api.base import RestApi

class CheckResultRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.isSuccess = None
			self.failedCode = None
			self.failedMsg = None

		def getapiname(self):
			return 'jingdong.checkResult'






