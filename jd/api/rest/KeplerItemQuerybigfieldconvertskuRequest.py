from jd.api.base import RestApi

class KeplerItemQuerybigfieldconvertskuRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.sku = None

		def getapiname(self):
			return 'jd.kepler.item.querybigfieldconvertsku'






