from jd.api.base import RestApi

class AfterSaleCustomerExpectCompQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.jdOrderId = None
			self.skuId = None

		def getapiname(self):
			return 'biz.afterSale.customerExpectComp.query'






