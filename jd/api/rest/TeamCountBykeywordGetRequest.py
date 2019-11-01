from jd.api.base import RestApi

class TeamCountBykeywordGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.key_word = None
			self.city_name = None
			self.is_team_external_url = None

		def getapiname(self):
			return 'jingdong.team.count.bykeyword.get'






