from jd.api.base import RestApi

class SearchWareRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.key = None
			self.filt_type = None
			self.area_ids = None
			self.sort_type = None
			self.page = None
			self.charset = None
			self.urlencode = None

		def getapiname(self):
			return 'jingdong.search.ware'






