from jd.api.base import RestApi

class ProductSkuQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.pageNum = None

		def getapiname(self):
			return 'biz.product.sku.query'






