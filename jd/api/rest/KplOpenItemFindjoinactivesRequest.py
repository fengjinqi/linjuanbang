from jd.api.base import RestApi

class KplOpenItemFindjoinactivesRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.uid = None
			self.sku = None

		def getapiname(self):
			return 'jd.kpl.open.item.findjoinactives'






