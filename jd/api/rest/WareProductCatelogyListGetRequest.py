from jd.api.base import RestApi

class WareProductCatelogyListGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.catelogyId = None

		def getapiname(self):
			return 'jingdong.ware.product.catelogy.list.get'






