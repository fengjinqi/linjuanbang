from jd.api.base import RestApi

class KplOpenWfpJmiwareUpdateWareStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.interfaceName = None
			self.methodName = None
			self.param = None

		def getapiname(self):
			return 'jd.kpl.open.wfp.jmiware.updateWareStatus'






