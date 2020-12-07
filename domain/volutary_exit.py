class VoluntaryExit:
    def __init__(self):
        self.epoch = None
        self.validator_index = None
        self.signature = None

    def csv_format(self):
        return (self.epoch,
                self.validator_index,
                self.signature)
