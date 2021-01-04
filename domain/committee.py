from utils.encode_tool import concat_array


class Committee:
    def __init__(self):
        self.epoch = None
        self.epoch_timestamp = None
        self.slot = None
        self.index = None
        self.committee = []

    def csv_format(self):
        return (self.epoch,
                self.epoch_timestamp,
                self.slot,
                self.index,
                concat_array(self.committee))
