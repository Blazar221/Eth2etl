class Validator(object):
    def __init__(self):
        self.pubkey = None
        self.validator_index = None
        self.balance = None

        self.withdrawal_credentials = None
        self.effective_balance = None
        self.slashed = False
        self.activation_eligibility_epoch = None
        self.activation_epoch = None
        self.exit_epoch = None
        self.withdrawable_epoch = None

    def csv_format(self):
        return (
            self.pubkey,
            self.validator_index,
            self.balance,
            self.withdrawal_credentials,
            self.effective_balance,
            self.slashed,
            self.activation_eligibility_epoch,
            self.activation_epoch,
            self.exit_epoch,
            self.withdrawable_epoch
        )
