from domain.beacon_block import BeaconBlock
from mapper.attestation_mapper import json_item_to_attestation
from mapper.attester_slashing_mapper import json_item_to_attester_slashing
from mapper.deposit_mapper import json_item_to_deposit
from mapper.proposer_slashing_mapper import json_item_to_proposer_slashing
from mapper.volutary_exit_mapper import json_item_to_volutary_exit
from constant import SLOT_PER_EPOCH
from utils.time_util import get_timestamp_slot


def create_block(json_item):
    block = BeaconBlock()
    block_outer = json_item['block']
    block_inner = block_outer['block']

    block.block_slot = int(block_inner['slot'])
    block.block_epoch = block.block_slot // SLOT_PER_EPOCH
    block.block_timestamp = get_timestamp_slot(block.block_slot)
    block.proposer_index = block_inner['proposerIndex']

    block.skipped = False

    block.block_root = json_item['blockRoot']
    block.parent_root = block_inner['parentRoot']
    block.state_root = block_inner['stateRoot']

    block.randao_reveal = block_inner['body']['randaoReveal']
    block.graffiti = block_inner['body']['graffiti']

    block.eth1_block_hash = block_inner['body']['eth1Data']['blockHash']
    block.eth1_deposit_root = block_inner['body']['eth1Data']['depositRoot']
    block.eth1_deposit_count = block_inner['body']['eth1Data']['depositCount']

    block.signature = block_outer['signature']

    block.attestations = [json_item_to_attestation(x)
                          for x in block_inner['body']['attestations']]
    block.deposits = [json_item_to_deposit(x)
                      for x in block_inner['body']['deposits']]
    block.proposer_slashings = [json_item_to_proposer_slashing(x)
                                for x in block_inner['body']['proposerSlashings']]
    block.attester_slashings = [json_item_to_attester_slashing(x)
                                for x in block_inner['body']['attesterSlashings']]
    block.voluntary_exits = [json_item_to_volutary_exit(x)
                             for x in block_inner['body']['voluntaryExits']]
    return block


def create_missed_block(slot):
    block = BeaconBlock()
    block.block_slot = slot
    block.block_epoch = slot // SLOT_PER_EPOCH
    block.block_timestamp = get_timestamp_slot(slot)
    block.skipped = True
    return block
