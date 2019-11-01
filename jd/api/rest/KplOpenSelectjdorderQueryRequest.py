from jd.api.base import RestApi

class KplOpenSelectjdorderQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.jdOrderId = None
			self.queryExts = None

		def getapiname(self):
			return 'jd.kpl.open.selectjdorder.query'






