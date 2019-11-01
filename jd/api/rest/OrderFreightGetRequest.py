from jd.api.base import RestApi

class OrderFreightGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.sku = None
			self.province = None
			self.city = None
			self.county = None
			self.town = None
			self.paymentType = None

		def getapiname(self):
			return 'biz.order.freight.get'






