from mapper.beacon_block_mapper import json_to_single_block
from mapper.committee_mapper import json_to_committees
from mapper.validator_mapper import json_array_to_validators
from service.api_service import get_block, get_committee, get_validator, get_validator_balance
from service.csv_service import save_blocks, save_committees, save_validators

import click
from time import time


@click.command()
@click.option('-h', '--slot-head', required=True, type=int, help='First slot to extract block')
@click.option('-e', '--slot-end', required=True, type=int, help='Last slot to extract block(not included)')
def extract_block(slot_head, slot_end):
    begin = time()
    blocks = [json_to_single_block(get_block(slot), slot)
              for slot in range(slot_head, slot_end)]
    save_blocks(blocks, slot_head, slot_end)
    print(f'Time cost on extracting blocks from slot{slot_head} to {slot_end}:{time() - begin}s')


@click.command()
@click.option('-h', '--epoch-head', required=True, type=int, help='First epoch to extract committee')
@click.option('-e', '--epoch-end', required=True, type=int, help='Last epoch to extract committee(not included)')
def extract_committee(epoch_head, epoch_end):
    begin = time()
    committees = []
    for epoch in range(epoch_head, epoch_end):
        committees.extend(json_to_committees(get_committee(epoch), epoch))
    save_committees(committees, epoch_head, epoch_end)
    print(f'Time cost on extracting committees from epoch{epoch_head} to {epoch_end}:{time() - begin}s')


@click.command()
@click.option('-e', '--epoch', required=True, type=int, help='The epoch to extract validator')
def extract_validator(epoch):
    begin = time()
    raw_vld = []
    for page in get_validator(epoch):
        raw_vld.extend(page['validatorList'])
    raw_balance = []
    for page in get_validator_balance(epoch):
        raw_balance.extend(page['balances'])
    validators = json_array_to_validators(raw_vld, raw_balance)
    save_validators(validators, epoch)
    print(f'Time cost on extracting validators at epoch{epoch}:{time() - begin}s')
