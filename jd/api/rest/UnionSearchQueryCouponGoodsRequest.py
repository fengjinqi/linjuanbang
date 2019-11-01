from jd.api.base import RestApi

class UnionSearchQueryCouponGoodsRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuIdList = None
			self.pageIndex = None
			self.pageSize = None
			self.cid3 = None
			self.goodsKeyword = None
			self.priceFrom = None
			self.priceTo = None

		def getapiname(self):
			return 'jingdong.union.search.queryCouponGoods'






