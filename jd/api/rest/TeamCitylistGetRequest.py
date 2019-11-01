from jd.api.base import RestApi

class TeamCitylistGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.feature = None

		def getapiname(self):
			return 'jingdong.team.citylist.get'






