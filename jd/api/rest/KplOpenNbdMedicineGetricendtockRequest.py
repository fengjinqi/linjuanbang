from jd.api.base import RestApi

class KplOpenNbdMedicineGetricendtockRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.medicineInfo = None
			self.hospitalCode = None

		def getapiname(self):
			return 'jd.kpl.open.nbd.medicine.getricendtock'






