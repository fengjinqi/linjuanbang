from jd.api.base import RestApi

class NewWareProductsortattGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuid = None

		def getapiname(self):
			return 'jingdong.new.ware.productsortatt.get'






