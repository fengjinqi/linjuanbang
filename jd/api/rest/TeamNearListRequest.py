from jd.api.base import RestApi

class TeamNearListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.longitude = None
			self.latitude = None
			self.radius = None
			self.isTeamExternalUrl = None
			self.client = None

		def getapiname(self):
			return 'jingdong.team.near.list'






