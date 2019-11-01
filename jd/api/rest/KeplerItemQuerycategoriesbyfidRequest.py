from jd.api.base import RestApi

class KeplerItemQuerycategoriesbyfidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.fid = None

		def getapiname(self):
			return 'jd.kepler.item.querycategoriesbyfid'






