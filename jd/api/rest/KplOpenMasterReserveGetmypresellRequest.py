from jd.api.base import RestApi

class KplOpenMasterReserveGetmypresellRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.client = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jd.kpl.open.master.reserve.getmypresell'






