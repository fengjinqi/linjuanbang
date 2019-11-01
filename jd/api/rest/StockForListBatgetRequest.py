from jd.api.base import RestApi

class StockForListBatgetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.sku = None
			self.area = None

		def getapiname(self):
			return 'biz.stock.forList.batget'






