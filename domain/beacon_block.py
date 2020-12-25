class BeaconBlock:
    def __init__(self):
        self.block_slot = None
        self.block_epoch = None
        self.block_timestamp = None
        self.proposer_index = None

        self.skipped = False

        self.block_root = None
        self.parent_root = None
        self.state_root = None

        self.randao_reveal = None
        self.graffiti = None

        self.eth1_block_hash = None
        self.eth1_deposit_root = None
        self.eth1_deposit_count = None

        self.signature = None

        self.attestations = []
        self.deposits = []
        self.proposer_slashings = []
        self.attester_slashings = []
        self.voluntary_exits = []

    def csv_format(self):
        return (self.block_slot,
                self.block_epoch,
                self.block_timestamp,
                self.proposer_index,
                self.skipped,
                self.block_root,
                self.parent_root,
                self.state_root,
                self.randao_reveal,
                self.graffiti,
                self.eth1_block_hash,
                self.eth1_deposit_root,
                self.eth1_deposit_count,
                self.signature)
