from mapper.beacon_block_mapper import json_to_single_block
from mapper.committee_mapper import json_to_committees
from mapper.validator_mapper import json_array_to_validators
from service.api_service import get_block, get_committee, get_validator, get_validator_balance
from service.csv_service import save_block, save_committees, save_validators
from time import time


def extract_block(slot):
    begin = time()
    save_block(json_to_single_block(get_block(slot), slot), slot)
    print(f'Time cost on extracting block on slot{slot}:{time() - begin}s')


def extract_committee(epoch):
    begin = time()
    committees = json_to_committees(get_committee(epoch), epoch)
    save_committees(committees, epoch)
    print(f'Time cost on extracting committees on epoch{epoch}:{time() - begin}s')


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
