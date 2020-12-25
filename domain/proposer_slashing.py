class ProposerSlashing:
    def __init__(self):
        self.header_1_slot = None
        self.header_1_proposer_index = None
        self.header_1_parent_root = None
        self.header_1_state_root = None
        self.header_1_body_root = None
        self.header_1_signature = None

        self.header_2_slot = None
        self.header_2_proposer_index = None
        self.header_2_parent_root = None
        self.header_2_state_root = None
        self.header_2_body_root = None
        self.header_2_signature = None

    def csv_format(self):
        return (self.header_1_slot,
                self.header_1_proposer_index,
                self.header_1_parent_root,
                self.header_1_state_root,
                self.header_1_body_root,
                self.header_1_signature,
                self.header_2_slot,
                self.header_2_proposer_index,
                self.header_2_parent_root,
                self.header_2_state_root,
                self.header_2_body_root,
                self.header_2_signature)
