from jd.api.base import RestApi

class KplOpenKeplerCartAddskustocartRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.commlist = None
			self.ybcommlist = None
			self.userid = None
			self.locationid = None
			self.type = None
			self.needCovert = None

		def getapiname(self):
			return 'jd.kpl.open.kepler.cart.addskustocart'






