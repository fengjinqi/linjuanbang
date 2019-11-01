from jd.api.base import RestApi

class ServicePromotionAppReportRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.time = None
			self.siteKey = None
			self.ext1 = None
			self.ext2 = None
			self.ext3 = None

		def getapiname(self):
			return 'jingdong.service.promotion.appReport'






