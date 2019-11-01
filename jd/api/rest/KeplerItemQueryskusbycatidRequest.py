from jd.api.base import RestApi

class KeplerItemQueryskusbycatidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.catId = None
			self.scrollId = None

		def getapiname(self):
			return 'jd.kepler.item.queryskusbycatid'






