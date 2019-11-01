from jd.api.base import RestApi

class PriceBalanceGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.payType = None

		def getapiname(self):
			return 'biz.price.balance.get'






