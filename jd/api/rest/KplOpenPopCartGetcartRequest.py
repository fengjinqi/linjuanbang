from jd.api.base import RestApi

class KplOpenPopCartGetcartRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.locationid = None
			self.skuList = None
			self.suitsList = None
			self.manJianList = None
			self.manZengList = None

		def getapiname(self):
			return 'jd.kpl.open.pop.cart.getcart'






