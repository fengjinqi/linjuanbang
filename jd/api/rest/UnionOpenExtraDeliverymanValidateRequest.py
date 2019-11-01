from jd.api.base import RestApi

class UnionOpenExtraDeliverymanValidateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.deliverymanReq = None

		def getapiname(self):
			return 'jd.union.open.extra.deliveryman.validate'






