class Deposit:
    def __init__(self):
        self.pubkey = None
        self.withdrawal_credentials = None
        self.amount = None
        self.signature = None

    def csv_format(self):
        return (self.pubkey,
                self.withdrawal_credentials,
                self.amount,
                self.signature)
