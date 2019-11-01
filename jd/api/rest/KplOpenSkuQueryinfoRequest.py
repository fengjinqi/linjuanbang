from jd.api.base import RestApi

class KplOpenSkuQueryinfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuQuery = None

		def getapiname(self):
			return 'jd.kpl.open.sku.queryinfo'






