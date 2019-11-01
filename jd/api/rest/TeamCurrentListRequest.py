from jd.api.base import RestApi

class TeamCurrentListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.cityId = None
			self.teamType = None
			self.areaId = None
			self.sqId = None
			self.groupId = None
			self.group2Id = None
			self.sort = None
			self.start = None
			self.limit = None
			self.isTeamExternalUrl = None
			self.client = None

		def getapiname(self):
			return 'jingdong.team.current.list'






