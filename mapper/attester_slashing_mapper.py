from domain.attester_slashing import AttesterSlashing


def json_item_to_attester_slashing(json_item):
    attester_slashings = AttesterSlashing()

    attestation1 = json_item['attestation1']

    attester_slashings.attestation_1_attesting_indices =\
        attestation1['attestingIndices']
    attester_slashings.attestation_1_slot = \
        attestation1['data']['slot']
    attester_slashings.attestation_1_index = \
        attestation1['data']['committeeIndex']
    attester_slashings.attestation_1_beacon_block_root =\
        attestation1['data']['beaconBlockRoot']
    attester_slashings.attestation_1_source_epoch =\
        attestation1['data']['source']['epoch']
    attester_slashings.attestation_1_source_root =\
        attestation1['data']['source']['root']
    attester_slashings.attestation_1_target_epoch =\
        attestation1['data']['target']['epoch']
    attester_slashings.attestation_1_target_root =\
        attestation1['data']['target']['root']
    attester_slashings.attestation_1_signature =\
        attestation1['signature']

    attestation2 = json_item['attestation2']
    attester_slashings.attestation_2_attesting_indices = \
        attestation2['attestingIndices']
    attester_slashings.attestation_2_slot = \
        attestation2['data']['slot']
    attester_slashings.attestation_2_index = \
        attestation2['data']['committeeIndex']
    attester_slashings.attestation_2_beacon_block_root = \
        attestation2['data']['beaconBlockRoot']
    attester_slashings.attestation_2_source_epoch = \
        attestation2['data']['source']['epoch']
    attester_slashings.attestation_2_source_root = \
        attestation2['data']['source']['root']
    attester_slashings.attestation_2_target_epoch = \
        attestation2['data']['target']['epoch']
    attester_slashings.attestation_2_target_root = \
        attestation2['data']['target']['root']
    attester_slashings.attestation_2_signature = \
        attestation2['signature']

    return attester_slashings
