from jd.api.base import RestApi

class ServicePromotionAppGetcodeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.jdurl = None
			self.appId = None
			self.subUnionId = None
			self.positionId = None
			self.ext = None
			self.protocol = None
			self.pid = None

		def getapiname(self):
			return 'jingdong.service.promotion.app.getcode'






