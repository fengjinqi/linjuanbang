from jd.api.base import RestApi

class KplOpenQuerypingpouGetcpsskubypageRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.pool = None
			self.size = None
			self.offset = None

		def getapiname(self):
			return 'jd.kpl.open.querypingpou.getcpsskubypage'






