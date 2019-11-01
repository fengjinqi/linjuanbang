from jd.api.base import RestApi

class BizProductGetSimilarSkuRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuId = None

		def getapiname(self):
			return 'jd.biz.product.getSimilarSku'






