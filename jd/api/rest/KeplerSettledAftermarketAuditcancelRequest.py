from jd.api.base import RestApi

class KeplerSettledAftermarketAuditcancelRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.serviceId = None
			self.approveNotes = None
			self.operatorInfo = None
			self.client = None

		def getapiname(self):
			return 'jd.kepler.settled.aftermarket.auditcancel'






