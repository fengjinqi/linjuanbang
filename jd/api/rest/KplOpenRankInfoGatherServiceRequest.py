from jd.api.base import RestApi

class KplOpenRankInfoGatherServiceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.clientParam = None
			self.rankParam = None

		def getapiname(self):
			return 'jingdong.kpl.open.RankInfoGatherService'






