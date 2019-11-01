from jd.api.base import RestApi

class KplOpenWeiboCartAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.xid = None
			self.url = None
			self.skuId = None
			self.ip = None
			self.appname = None
			self.timestamp = None
			self.deviceid = None
			self.token = None
			self.sessionid = None
			self.signature = None
			self.applicationname = None
			self.packagename = None
			self.applicationmd5 = None
			self.ua = None
			self.os = None
			self.osversion = None

		def getapiname(self):
			return 'jd.kpl.open.weibo.cart.add'






