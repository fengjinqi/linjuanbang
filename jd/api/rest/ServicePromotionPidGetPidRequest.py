from jd.api.base import RestApi

class ServicePromotionPidGetPidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.positionName = None
			self.promotionType = None
			self.unionId = None
			self.sonUnionId = None
			self.mediaName = None

		def getapiname(self):
			return 'jingdong.service.promotion.pid.getPid'






