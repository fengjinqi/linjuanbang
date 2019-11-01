from jd.api.base import RestApi

class KplOpenCommentCommentlistRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.param = None

		def getapiname(self):
			return 'jd.kpl.open.comment.commentlist'






