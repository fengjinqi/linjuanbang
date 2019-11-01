from jd.api.base import RestApi

class ServicePromotionQueryPromotionSiteRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.unionId = None
			self.key = None
			self.unionType = None
			self.pageNo = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.service.promotion.queryPromotionSite'






