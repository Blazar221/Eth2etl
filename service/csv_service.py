import csv
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

    _save_csv(f'blocks/blocks_{slot}_{day}', [block_data])
    _save_csv(f'blocks/attestations_{slot}_{day}', attestation_data)
    _save_csv(f'blocks/attester_slashings_{slot}_{day}', attester_slashing_data)
    _save_csv(f'blocks/deposits_{slot}_{day}', deposit_data)
    _save_csv(f'blocks/proposer_slashings_{slot}_{day}', proposer_slashing_data)
    _save_csv(f'blocks/voluntary_exits_{slot}_{day}', voluntary_exit_data)


def save_committees(committees, epoch):
    day = get_day_epoch(epoch)
    committee_data = [cmt.csv_format() for cmt in committees]
    _save_csv(f'committees/committees_{epoch}_{day}', committee_data)


def save_validators(validators, epoch):
    day = get_day_epoch(epoch)
    validator_data = [vld.csv_format() for vld in validators]
    _save_csv(f"validators/validators_{epoch}_{day}", validator_data)


def _append_field(field: tuple, extra: tuple):
    return (*field, *extra)


def _save_csv(filename, data):
    if data:
        with open(CSV_PATH + filename + '.csv', 'a') as f:
            writer = csv.writer(f)
            for line in data:
                writer.writerow(line)
