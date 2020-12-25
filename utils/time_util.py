import time
from constant import SECOND_PER_SLOT, SLOT_PER_EPOCH
from service.api_service import get_genesis_detail

OFFSET_SECONDS_CHINA_FROM_UTC = 8 * 60 * 60

GENESIS_TIMESTAMP = OFFSET_SECONDS_CHINA_FROM_UTC + time.mktime(
    time.strptime(get_genesis_detail()['genesisTime'], '%Y-%m-%dT%H:%M:%SZ'))


def get_day_str(slot):
    time_stamp = GENESIS_TIMESTAMP + slot * SECOND_PER_SLOT
    return time.strftime('%Y-%m-%d', time.localtime(time_stamp))


def get_timestamp_slot(slot: int):
    return GENESIS_TIMESTAMP + slot * SECOND_PER_SLOT


def get_timestamp_epoch(epoch: int):
    return GENESIS_TIMESTAMP + epoch * SECOND_PER_SLOT * SLOT_PER_EPOCH
