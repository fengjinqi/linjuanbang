from jd.api.base import RestApi

class KplOpenGetsellpriceQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.sku = None
			self.containsTax = None
			self.queryExts = None

		def getapiname(self):
			return 'jd.kpl.open.getsellprice.query'






