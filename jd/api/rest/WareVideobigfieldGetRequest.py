from jd.api.base import RestApi

class WareVideobigfieldGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuId = None

		def getapiname(self):
			return 'jingdong.ware.videobigfield.get'






