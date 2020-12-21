import csv
from config import CSV_PATH


def save_block(block, slot):
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

    _save_csv(f'blocks_{slot}', block_data)
    _save_csv(f'attestations_{slot}', attestation_data)
    _save_csv(f'attester_slashings_{slot}', attester_slashing_data)
    _save_csv(f'deposits_{slot}', deposit_data)
    _save_csv(f'proposer_slashings_{slot}', proposer_slashing_data)
    _save_csv(f'voluntary_exits_{slot}', voluntary_exit_data)


def save_committees(committees, epoch):
    _save_csv(f'committees_{epoch}', committees.csv_format())


def save_validators(validators, epoch):
    validator_data = [vld.csv_format() for vld in validators]
    _save_csv(f"validators_{epoch}", validator_data)


def _append_field(field: tuple, extra: tuple):
    return (*field, *extra)


def _save_csv(filename, data):
    if data:
        with open(CSV_PATH + filename + '.csv', 'a') as f:
            writer = csv.writer(f)
            for line in data:
                writer.writerow(line)
