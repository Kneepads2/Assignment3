
class Account:
    def __init__(self,_accountNumber,_accountHolderName,_rateOfInterest,_currentBalance):
        self.accountNumber = _accountNumber
        self.accountHolderName = _accountHolderName
        self.rateOfInterest = _rateOfInterest
        self.currentBalance = _currentBalance

    def getAccountNumber(self):
        return self.accountNumber

    def getAccountHolderName(self):
        return self.accountHolderName

    def getRateOfInterest(self):
        return self.rateOfInterest

    def getCurrentBalance(self):
        return self.currentBalance

    def disposit(self):
        print("")

    def withdraw(self):
        print("")