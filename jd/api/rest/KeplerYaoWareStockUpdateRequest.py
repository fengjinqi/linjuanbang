from jd.api.base import RestApi

class KeplerYaoWareStockUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.wareList = None

		def getapiname(self):
			return 'jd.kepler.yao.ware.stock.update'






