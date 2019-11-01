from jd.api.base import RestApi

class ProductBaseQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.sku = None
			self.areaId = None

		def getapiname(self):
			return 'public.product.base.query'






