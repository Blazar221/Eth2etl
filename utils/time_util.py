import time
from constant import SECOND_PER_SLOT, SLOT_PER_EPOCH
from config import GENESIS_TIMESTAMP


def get_day_slot(slot: int):
    print(time.strftime('%Y-%m-%d %HH:%MM:%SS', time.localtime(get_timestamp_slot(slot))))
    return time.strftime('%Y-%m-%d', time.localtime(get_timestamp_slot(slot)))


def get_day_epoch(epoch: int):
    return time.strftime('%Y-%m-%d', time.localtime(get_timestamp_epoch(epoch)))


def get_timestamp_slot(slot: int):
    return GENESIS_TIMESTAMP + slot * SECOND_PER_SLOT


def get_timestamp_epoch(epoch: int):
    return GENESIS_TIMESTAMP + epoch * SECOND_PER_SLOT * SLOT_PER_EPOCH


def check_genesis_time():
    genesis_time = '2020-12-01 12:00:23'
    return genesis_time == time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(GENESIS_TIMESTAMP))

