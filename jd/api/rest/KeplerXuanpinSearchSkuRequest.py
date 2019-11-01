from jd.api.base import RestApi

class KeplerXuanpinSearchSkuRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.queryParam = None
			self.pageParam = None
			self.orderField = None

		def getapiname(self):
			return 'jd.kepler.xuanpin.search.sku'






