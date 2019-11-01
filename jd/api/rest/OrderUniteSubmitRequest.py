from jd.api.base import RestApi

class OrderUniteSubmitRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.thirdOrder = None
			self.sku = None
			self.name = None
			self.province = None
			self.city = None
			self.county = None
			self.town = None
			self.address = None
			self.zip = None
			self.phone = None
			self.mobile = None
			self.email = None
			self.remark = None
			self.invoiceState = None
			self.invoiceType = None
			self.selectedInvoiceTitle = None
			self.companyName = None
			self.invoiceContent = None
			self.paymentType = None
			self.isUseBalance = None
			self.submitState = None
			self.invoiceName = None
			self.invoicePhone = None
			self.invoiceProvice = None
			self.invoiceCity = None
			self.invoiceCounty = None
			self.invoiceAddress = None
			self.doOrderPriceMode = None
			self.orderPriceSnap = None
			self.extContent = None

		def getapiname(self):
			return 'biz.order.unite.submit'






