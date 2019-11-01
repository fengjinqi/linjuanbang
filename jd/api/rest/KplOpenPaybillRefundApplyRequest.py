from jd.api.base import RestApi

class KplOpenPaybillRefundApplyRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.refundVO = None

		def getapiname(self):
			return 'jd.kpl.open.paybill.refund.apply'






