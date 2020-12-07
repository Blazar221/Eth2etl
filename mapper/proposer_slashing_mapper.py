from domain.proposer_slashing import ProposerSlashing


def json_item_to_proposer_slashing(json_item):
    proposerSlashing = ProposerSlashing()
    header1 = json_item['header1']
    proposerSlashing.header_1_slot =\
        header1['header']['slot']
    proposerSlashing.header_1_proposer_index =\
        header1['header']['proposerIndex']
    proposerSlashing.header_1_parent_root =\
        header1['header']['parentRoot']
    proposerSlashing.header_1_state_root =\
        header1['header']['stateRoot']
    proposerSlashing.header_1_body_root =\
        header1['header']['bodyRoot']
    proposerSlashing.header_1_signature = header1['signature']

    header2 = json_item['header2']
    proposerSlashing.header_2_slot =\
        header2['header']['slot']
    proposerSlashing.header_2_proposer_index =\
        header2['header']['proposerIndex']
    proposerSlashing.header_2_parent_root =\
        header2['header']['parentRoot']
    proposerSlashing.header_2_state_root =\
        header2['header']['stateRoot']
    proposerSlashing.header_2_body_root =\
        header2['header']['bodyRoot']
    proposerSlashing.header_2_signature = header2['signature']

    return proposerSlashing
