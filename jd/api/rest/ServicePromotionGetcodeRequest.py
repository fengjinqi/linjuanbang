from jd.api.base import RestApi

class ServicePromotionGetcodeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.promotionType = None
			self.materialId = None
			self.unionId = None
			self.subUnionId = None
			self.siteSize = None
			self.siteId = None
			self.channel = None
			self.webId = None
			self.extendId = None
			self.ext1 = None
			self.adttype = None
			self.protocol = None
			self.pid = None

		def getapiname(self):
			return 'jingdong.service.promotion.getcode'






