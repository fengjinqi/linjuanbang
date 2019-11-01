from jd.api.base import RestApi

class InvoiceQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.markId = None

		def getapiname(self):
			return 'biz.invoice.query'






