from jd.api.base import RestApi

class KplOpenXuanpinSearchSkuRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.queryParam = None
			self.pageParam = None
			self.orderField = None
			self.order = None

		def getapiname(self):
			return 'jd.kpl.open.xuanpin.search.sku'






