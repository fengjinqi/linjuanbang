from jd.api.base import RestApi

class ProductIsCodQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuIds = None
			self.province = None
			self.city = None
			self.town = None
			self.county = None

		def getapiname(self):
			return 'biz.product.isCod.query'






