from jd.api.base import RestApi

class UnionOrderServiceQueryCommisionsRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.time = None
			self.pageIndex = None
			self.pageSize = None
			self.unionId = None

		def getapiname(self):
			return 'jingdong.UnionOrderService.queryCommisions'






