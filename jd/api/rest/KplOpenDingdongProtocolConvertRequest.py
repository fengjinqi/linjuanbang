from jd.api.base import RestApi

class KplOpenDingdongProtocolConvertRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.inputStr = None
			self.appId = None

		def getapiname(self):
			return 'jd.kpl.open.dingdong.protocol.convert'






