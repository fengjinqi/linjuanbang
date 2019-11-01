from jd.api.base import RestApi

class InvoiceSubmitRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.supplierOrder = None
			self.markId = None
			self.settlementId = None
			self.settlementNum = None
			self.settlementNakedPrice = None
			self.settlementTaxPrice = None
			self.invoiceType = None
			self.invoiceOrg = None
			self.bizInvoiceContent = None
			self.invoiceDate = None
			self.title = None
			self.billToParty = None
			self.enterpriseTaxpayer = None
			self.billToer = None
			self.billToContact = None
			self.billToProvince = None
			self.billToCity = None
			self.billToCounty = None
			self.billToTown = None
			self.billToAddress = None
			self.repaymentDate = None
			self.invoiceNum = None
			self.invoiceNakedPrice = None
			self.invoiceTaxPrice = None
			self.currentBatch = None
			self.totalBatch = None
			self.totalBatchInvoiceNakedAmount = None
			self.totalBatchInvoiceTaxAmount = None
			self.totalBatchInvoiceAmount = None
			self.billingType = None
			self.invoicePrice = None
			self.isMerge = None
			self.poNo = None
			self.enterpriseRegAddress = None
			self.enterpriseRegPhone = None
			self.enterpriseBankName = None
			self.enterpriseBankAccount = None

		def getapiname(self):
			return 'biz.invoice.submit'






