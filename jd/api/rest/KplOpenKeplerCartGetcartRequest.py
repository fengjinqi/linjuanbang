from jd.api.base import RestApi

class KplOpenKeplerCartGetcartRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.userid = None
			self.locationid = None

		def getapiname(self):
			return 'jd.kpl.open.kepler.cart.getcart'






