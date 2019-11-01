from jd.api.base import RestApi

class ServicePromotionContentGetcodeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.releaseType = None
			self.typeId = None
			self.sortName = None
			self.sort = None
			self.pageSize = None
			self.pageIndex = None
			self.unionId = None
			self.subUnionId = None
			self.webId = None
			self.ext1 = None
			self.protocol = None
			self.positionId = None

		def getapiname(self):
			return 'jingdong.service.promotion.content.getcode'






