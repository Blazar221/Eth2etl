class Attestation:
    def __init__(self):
        self.aggregation_bits = None
        self.slot = None
        self.index = None
        self.beacon_block_root = None

        self.source_epoch = None
        self.source_root = None
        self.target_epoch = None
        self.target_root = None

        self.signature = None

    def csv_format(self):
        return (self.aggregation_bits,
                self.slot,
                self.index,
                self.beacon_block_root,
                self.source_epoch,
                self.source_root,
                self.target_epoch,
                self.target_root,
                self.signature)
