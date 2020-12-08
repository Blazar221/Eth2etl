import csv
from config import CSV_PATH


def save_blocks(blocks, slot_head, slot_end):
    block_data = []
    attestation_data = []
    attester_slashing_data = []
    deposit_data = []
    proposer_slashing_data = []
    voluntary_exit_data = []
    for block in blocks:
        block_data.append(block.csv_format())

        extra_field = (block.block_slot, block.block_timestamp)

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
    file_slot_id = f'{slot_head}_{slot_end}'
    _save_csv(f'blocks_{file_slot_id}', block_data)
    _save_csv(f'attestations_{file_slot_id}', attestation_data)
    _save_csv(f'attester_slashings_{file_slot_id}', attester_slashing_data)
    _save_csv(f'deposits_{file_slot_id}', deposit_data)
    _save_csv(f'proposer_slashings_{file_slot_id}', proposer_slashing_data)
    _save_csv(f'voluntary_exits_{file_slot_id}', voluntary_exit_data)


def _append_field(field: tuple, extra: tuple):
    return (*field, *extra)


def _save_csv(filename, data):
    if data:
        with open(CSV_PATH + filename + '.csv', 'a') as f:
            writer = csv.writer(f)
            for line in data:
                writer.writerow(line)
