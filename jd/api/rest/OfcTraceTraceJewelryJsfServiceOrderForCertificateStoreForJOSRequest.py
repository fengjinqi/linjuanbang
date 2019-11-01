from jd.api.base import RestApi

class OfcTraceTraceJewelryJsfServiceOrderForCertificateStoreForJOSRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.certificateTypeCode = None
			self.orderId = None
			self.institutionCode = None
			self.groupId = None
			self.securityCode = None
			self.certificateNo = None
			self.skuId = None
			self.certificateType = None

		def getapiname(self):
			return 'jingdong.ofc.trace.traceJewelryJsfService.orderForCertificateStoreForJOS'






