from jd.api.base import RestApi

class TeamPromotionSameListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.teamId = None
			self.cityId = None
			self.client = None

		def getapiname(self):
			return 'jingdong.team.promotion.same.list'






