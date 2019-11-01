from jd.api.base import RestApi

class WareProductbigfieldGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.sku_id = None
			self.field = None

		def getapiname(self):
			return 'jingdong.ware.productbigfield.get'






