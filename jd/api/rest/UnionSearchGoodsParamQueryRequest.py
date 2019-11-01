from jd.api.base import RestApi

class UnionSearchGoodsParamQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.cat1Id = None
			self.owner = None
			self.pageIndex = None
			self.pageSize = None
			self.sortName = None
			self.sort = None
			self.skuIds = None
			self.pingouPriceStart = None
			self.pingouPriceEnd = None
			self.wlCommissionShareStart = None
			self.wlCommissionShareEnd = None

		def getapiname(self):
			return 'jingdong.union.search.goods.param.query'






