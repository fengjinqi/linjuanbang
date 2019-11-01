from jd.api.base import RestApi

class ServicePromotionQueryDesignboomGoodsRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.state = None
			self.sort = None
			self.desc = None
			self.pageNo = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.service.promotion.queryDesignboomGoods'






