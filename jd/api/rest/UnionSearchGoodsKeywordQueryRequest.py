from jd.api.base import RestApi

class UnionSearchGoodsKeywordQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.cat1Id = None
			self.cat2Id = None
			self.cat3Id = None
			self.keyword = None
			self.page_index = None
			self.page_size = None
			self.sort_name = None
			self.sort = None

		def getapiname(self):
			return 'jingdong.union.search.goods.keyword.query'






