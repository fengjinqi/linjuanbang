from jd.api.base import RestApi

class ServiceYhdPromotionGetInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.proCont = None
			self.materialId = None
			self.unionId = None
			self.subUnionId = None
			self.webId = None
			self.ext1 = None
			self.positionId = None
			self.protocol = None

		def getapiname(self):
			return 'jingdong.service.yhd.promotion.getInfo'






