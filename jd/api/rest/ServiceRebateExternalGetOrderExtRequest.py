from jd.api.base import RestApi

class ServiceRebateExternalGetOrderExtRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.unionId = None
			self.orderId = None
			self.skuId = None

		def getapiname(self):
			return 'jingdong.service.rebate.external.getOrderExt'






