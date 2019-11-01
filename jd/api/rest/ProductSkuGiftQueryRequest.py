from jd.api.base import RestApi

class ProductSkuGiftQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.province = None
			self.city = None
			self.county = None
			self.town = None

		def getapiname(self):
			return 'biz.product.skuGift.query'






