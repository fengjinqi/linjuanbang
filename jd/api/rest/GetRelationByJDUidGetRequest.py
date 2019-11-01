from jd.api.base import RestApi

class GetRelationByJDUidGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.uid = None

		def getapiname(self):
			return 'jingdong.getRelationByJDUid.get'






