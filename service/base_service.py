from mapper.beacon_block_mapper import create_block, create_missed_block
from mapper.committee_mapper import json_to_committees
from mapper.validator_mapper import json_array_to_validators
from service.api_service import get_block, get_committee, get_validator, get_validator_balance, get_genesis_detail, get_chainhead
from service.csv_service import save_block, save_committees, save_validators, save_multiple_block
from utils.time_util import check_genesis_time
from time import time


def extract_block(slot):
    head_slot = int(get_chainhead()['headSlot'])
    begin = time()
    container = get_block(slot)['blockContainers']
    if 0 == len(container):
      save_block(create_missed_block(slot), slot)
    elif 1 == len(container):
      save_block(create_block(container[0]), slot)
    else:
      blocks = []
      for each in container:
        blocks.append(create_block(each))
      save_multiple_block(blocks, slot)
    print('Time cost on extracting block on slot{}:{}s'.format(slot, time()-begin))


def extract_committee(epoch):
    head_epoch = int(get_chainhead()['headEpoch'])
    begin = time()
    committees = json_to_committees(get_committee(epoch), epoch)
    save_committees(committees, epoch)
    print('Time cost on extracting committees on epoch{}:{}s'.format(epoch, time()-begin))


def extract_validator(epoch):
    head_epoch = int(get_chainhead()['headEpoch'])
    begin = time()
    raw_vld = []
    for page in get_validator(epoch):
        raw_vld.extend(page['validatorList'])
    raw_balance = []
    for page in get_validator_balance(epoch):
        raw_balance.extend(page['balances'])
    validators = json_array_to_validators(raw_vld, raw_balance)
    save_validators(validators, epoch)
    print('Time cost on extracting validators at epoch{}:{}s'.format(epoch, time()-begin))


def quest_genesis():
    print(get_genesis_detail())


def quest_chainhead():
    print(get_chainhead())


def check_time():
    print(check_genesis_time())


def check_slot(slot):
    print(slot <= int(get_chainhead()['headSlot']))
