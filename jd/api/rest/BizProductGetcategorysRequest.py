from jd.api.base import RestApi

class BizProductGetcategorysRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.pageNo = None
			self.pageSize = None
			self.parentId = None
			self.catClass = None

		def getapiname(self):
			return 'jd.biz.product.getcategorys'






