from jd.api.base import RestApi

class AfterSaleServiceDetailInfoQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.afsServiceId = None
			self.appendInfoSteps = None

		def getapiname(self):
			return 'biz.afterSale.serviceDetailInfo.query'






