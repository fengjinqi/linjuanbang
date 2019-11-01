from jd.api.base import RestApi

class CreatePromotionSiteJosSaveAppPromtionSiteInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.pin = None
			self.appId = None
			self.adName = None
			self.adType = None
			self.adSize = None

		def getapiname(self):
			return 'jingdong.CreatePromotionSiteJos.saveAppPromtionSiteInfo'






