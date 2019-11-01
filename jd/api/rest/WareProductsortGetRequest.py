from jd.api.base import RestApi

class WareProductsortGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.product_sort_ids = None

		def getapiname(self):
			return 'jingdong.ware.productsort.get'






