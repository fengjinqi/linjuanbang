from jd.api.base import RestApi

class KeplerItemGetnologinpromotionRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuids = None
			self.area = None
			self.venderId = None
			self.appid = None

		def getapiname(self):
			return 'jd.kepler.item.getnologinpromotion'






