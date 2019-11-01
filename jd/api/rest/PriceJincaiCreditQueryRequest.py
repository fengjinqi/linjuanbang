from jd.api.base import RestApi

class PriceJincaiCreditQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)

		def getapiname(self):
			return 'biz.price.jincaiCredit.query'






