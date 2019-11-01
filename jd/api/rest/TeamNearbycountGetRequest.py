from jd.api.base import RestApi

class TeamNearbycountGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.longitude = None
			self.latitude = None
			self.radius = None
			self.is_team_external_url = None

		def getapiname(self):
			return 'jingdong.team.nearbycount.get'






