from jd.api.base import RestApi

class KplOpenShopGoodsListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.goodsSearchParam = None

		def getapiname(self):
			return 'jd.kpl.open.shop.goods.list'






