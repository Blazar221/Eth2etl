from mapper.beacon_block_mapper import json_to_single_block
from mapper.committee_mapper import json_to_committees
from mapper.validator_mapper import json_array_to_validators
from service.api_service import get_block, get_committee, get_validator, get_validator_balance
from service.csv_service import save_blocks, save_committees, save_validators


def extract_block(slot_head, slot_end):
    blocks = [json_to_single_block(get_block(slot), slot)
              for slot in range(slot_head, slot_end)]
    save_blocks(blocks, slot_head, slot_end)


def extract_committee(epoch_head, epoch_end):
    committees = []
    for epoch in range(epoch_head, epoch_end):
        committees.extend(json_to_committees(get_committee(epoch), epoch))
    save_committees(committees, epoch_head, epoch_end)


def extract_validator(epoch):
    raw_vld = []
    response_json = get_validator(epoch)
    while response_json['nextPageToken']:
        raw_vld.extend(response_json['validatorList'])
        response_json = get_validator(epoch, page_token=response_json['nextPageToken'])
    raw_vld.extend(response_json['validatorList'])
    raw_balance = []
    response_json = get_validator_balance(epoch)
    while response_json['nextPageToken']:
        raw_balance.extend(response_json['balances'])
        response_json = get_validator_balance(epoch, page_token=response_json['nextPageToken'])
    raw_balance.extend(response_json['balances'])
    validators = json_array_to_validators(raw_vld, raw_balance)
    save_validators(validators, epoch)
