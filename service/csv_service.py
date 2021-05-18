import csv
import os
from config import CSV_PATH
from utils.time_util import get_day_slot, get_day_epoch


def save_block(block, slot):
    day = get_day_slot(slot)

    block_data = block.csv_format()

    extra_field = (block.block_slot, block.block_timestamp)

    attestation_data = [_append_field(attestation.csv_format(), extra_field)
                        for attestation in block.attestations]
    attester_slashing_data = [_append_field(attester_slashing.csv_format(), extra_field) for attester_slashing
                              in block.attester_slashings]
    deposit_data = [_append_field(deposit.csv_format(), extra_field) for deposit
                    in block.deposits]
    proposer_slashing_data = [_append_field(proposer_slashing.csv_format(), extra_field) for proposer_slashing
                              in block.proposer_slashings]
    voluntary_exit_data = [_append_field(voluntary_exit.csv_format(), extra_field) for voluntary_exit
                           in block.voluntary_exits]

    _save_csv('blocks_{}_{}'.format(slot, day), [block_data])
    _save_csv('attestations_{}_{}'.format(slot, day), attestation_data)
    _save_csv('attester_slashings_{}_{}'.format(slot, day), attester_slashing_data)
    _save_csv('deposits_{}_{}'.format(slot, day), deposit_data)
    _save_csv('proposer_slashings_{}_{}'.format(slot, day), proposer_slashing_data)
    _save_csv('voluntary_exits_{}_{}'.format(slot, day), voluntary_exit_data)
    

def save_multiple_block(blocks, slot):
    day = get_day_slot(slot)
    block_data = []
    attestation_data = []
    attester_slashing_data = []
    deposit_data = []
    proposer_slashing_data = []
    voluntary_exit_data = []
    
    extra_field = (blocks[0].block_slot, blocks[0].block_timestamp)
    for block in blocks:
      block_data.append(block.csv_format())
      attestation_data.extend([_append_field(attestation.csv_format(), extra_field)
                        for attestation in block.attestations])
      attester_slashing_data.extend([_append_field(attester_slashing.csv_format(), extra_field) for attester_slashing
                              in block.attester_slashings])
      deposit_data.extend([_append_field(deposit.csv_format(), extra_field) for deposit
                    in block.deposits])
      proposer_slashing_data.extend([_append_field(proposer_slashing.csv_format(), extra_field) for proposer_slashing
                              in block.proposer_slashings])
      voluntary_exit_data.extend([_append_field(voluntary_exit.csv_format(), extra_field) for voluntary_exit
                           in block.voluntary_exits])

    _save_csv('blocks_{}_{}'.format(slot, day), block_data)
    _save_csv('attestations_{}_{}'.format(slot, day), attestation_data)
    _save_csv('attester_slashings_{}_{}'.format(slot, day), attester_slashing_data)
    _save_csv('deposits_{}_{}'.format(slot, day), deposit_data)
    _save_csv('proposer_slashings_{}_{}'.format(slot, day), proposer_slashing_data)
    _save_csv('voluntary_exits_{}_{}'.format(slot, day), voluntary_exit_data)

def save_committees(committees, epoch):
    day = get_day_epoch(epoch)
    committee_data = [cmt.csv_format() for cmt in committees]
    _save_csv('committees_{}_{}'.format(epoch, day), committee_data)


def save_validators(validators, epoch):
    day = get_day_epoch(epoch)
    validator_data = [(*vld.csv_format(), epoch) for vld in validators]
    _save_csv('validators_{}_{}'.format(epoch, day), validator_data)


def _append_field(field: tuple, extra: tuple):
    return (*field, *extra)


def _save_csv(filename, data):
    if data:
        file_prefix = CSV_PATH + filename
        with open(file_prefix + '.part', 'w') as f:
            writer = csv.writer(f)
            for line in data:
                writer.writerow(line)
        os.rename(file_prefix + '.part', file_prefix + '.csv')


