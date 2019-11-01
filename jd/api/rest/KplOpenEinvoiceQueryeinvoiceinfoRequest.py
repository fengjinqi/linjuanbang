from jd.api.base import RestApi

class KplOpenEinvoiceQueryeinvoiceinfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.eInvoiceQueryWs = None

		def getapiname(self):
			return 'jd.kpl.open.einvoice.queryeinvoiceinfo'






