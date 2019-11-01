from jd.api.base import RestApi

class KplOpenRegularPlanCompletedorderRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.planId = None
			self.orderId = None

		def getapiname(self):
			return 'jd.kpl.open.regular.plan.completedorder'






