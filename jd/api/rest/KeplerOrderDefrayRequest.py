from jd.api.base import RestApi

class KeplerOrderDefrayRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.defrayReqParam = None

		def getapiname(self):
			return 'jd.kepler.order.defray'






