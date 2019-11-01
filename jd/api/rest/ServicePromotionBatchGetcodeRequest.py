from jd.api.base import RestApi

class ServicePromotionBatchGetcodeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.id = None
			self.url = None
			self.unionId = None
			self.subUnionId = None
			self.channel = None
			self.webId = None
			self.positionId = None
			self.ext1 = None
			self.protocol = None
			self.pid = None

		def getapiname(self):
			return 'jingdong.service.promotion.batch.getcode'






