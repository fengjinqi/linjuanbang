from jd.api.base import RestApi

class ServiceGoodsQueryStuPriceGoodsRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuIdList = None
			self.pageIndex = None
			self.pageSize = None
			self.stuPriceFrom = None
			self.stuPriceTo = None
			self.cid1Id = None
			self.cid2Id = None
			self.cid3Id = None
			self.owner = None
			self.commissionShareFrom = None
			self.commissionShareTo = None
			self.sortName = None
			self.sort = None

		def getapiname(self):
			return 'jingdong.service.goods.queryStuPriceGoods'






