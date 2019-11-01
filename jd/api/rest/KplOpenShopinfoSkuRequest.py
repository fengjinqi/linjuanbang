from jd.api.base import RestApi

class KplOpenShopinfoSkuRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.set = None

		def getapiname(self):
			return 'jd.kpl.open.shopinfo.sku'






