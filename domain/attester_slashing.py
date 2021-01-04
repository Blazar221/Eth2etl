from utils.encode_tool import concat_array

class AttesterSlashing:
    def __init__(self):
        self.attestation_1_attesting_indices = []
        self.attestation_1_slot = None
        self.attestation_1_index = None
        self.attestation_1_beacon_block_root = None
        self.attestation_1_source_epoch = None
        self.attestation_1_source_root = None
        self.attestation_1_target_epoch = None
        self.attestation_1_target_root = None
        self.attestation_1_signature = None

        self.attestation_2_attesting_indices = []
        self.attestation_2_slot = None
        self.attestation_2_index = None
        self.attestation_2_beacon_block_root = None
        self.attestation_2_source_epoch = None
        self.attestation_2_source_root = None
        self.attestation_2_target_epoch = None
        self.attestation_2_target_root = None
        self.attestation_2_signature = None

    def csv_format(self):
        return (concat_array(self.attestation_1_attesting_indices),
                self.attestation_1_slot,
                self.attestation_1_index,
                self.attestation_1_beacon_block_root,
                self.attestation_1_source_epoch,
                self.attestation_1_source_root,
                self.attestation_1_target_epoch,
                self.attestation_1_target_root,
                self.attestation_1_signature,
                concat_array(self.attestation_2_attesting_indices),
                self.attestation_2_slot,
                self.attestation_2_index,
                self.attestation_2_beacon_block_root,
                self.attestation_2_source_epoch,
                self.attestation_2_source_root,
                self.attestation_2_target_epoch,
                self.attestation_2_target_root,
                self.attestation_2_signature)
