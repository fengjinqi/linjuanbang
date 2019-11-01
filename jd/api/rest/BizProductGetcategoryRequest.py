from jd.api.base import RestApi

class BizProductGetcategoryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.cid = None

		def getapiname(self):
			return 'jd.biz.product.getcategory'






