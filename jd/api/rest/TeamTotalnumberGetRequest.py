from jd.api.base import RestApi

class TeamTotalnumberGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.city_id = None
			self.group_id = None
			self.team_type = None
			self.district_id = None
			self.area_id = None
			self.group2_id = None
			self.is_team_external_url = None

		def getapiname(self):
			return 'jingdong.team.totalnumber.get'






