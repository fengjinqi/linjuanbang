from jd.api.base import RestApi

class UnionSearchGoodsCategoryQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.parent_id = None
			self.grade = None

		def getapiname(self):
			return 'jingdong.union.search.goods.category.query'






