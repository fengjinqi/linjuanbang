from jd.api.base import RestApi

class KeplerXuanpinSearchSkuByCategoryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.category = None
			self.pageSize = None
			self.pageNo = None

		def getapiname(self):
			return 'jd.kepler.xuanpin.search.sku.by.category'






