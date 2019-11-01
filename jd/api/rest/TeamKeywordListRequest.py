from jd.api.base import RestApi

class TeamKeywordListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.keyWord = None
			self.cityName = None
			self.start = None
			self.limit = None
			self.isTeamExternalUrl = None
			self.client = None

		def getapiname(self):
			return 'jingdong.team.keyword.list'






