from jd.api.base import RestApi

class UnionOpenPositionQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.positionReq = None

		def getapiname(self):
			return 'jd.union.open.position.query'






