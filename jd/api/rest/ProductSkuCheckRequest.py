from jd.api.base import RestApi

class ProductSkuCheckRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuIds = None
			self.queryExts = None

		def getapiname(self):
			return 'biz.product.sku.check'






