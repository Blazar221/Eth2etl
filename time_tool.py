import time
import pytz
from constant import GENESIS_TIME_STAMP, SECOND_OF_SLOT, SLOT_PER_EPOCH

''' 
The genesis time of mainnet is just equal to the origin time in Python time module, namely 1970-01-01. But in future the genesis time may change depended on the net used. 
Another issue is that 1970-01-01 comes from which time zone? The evidence indicates that it is the standard Greenwich Time, which means that 1970-01-01 00:00:00 is equal to the Shanghai time 1970-01-01 08:00:00
Final issue: the time stamp in csv in which format?
'''
def get_day_str(slot):
	time_stamp = GENESIS_TIME_STAMP + slot * SECOND_OF_SLOT
	return time.strftime('%Y-%m-%d', time.localtime(time_stamp))


def get_timestamp_slot(slot):
	time_stamp = GENESIS_TIME_STAMP + slot * SECOND_OF_SLOT
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_stamp))


def get_timestamp_epoch(epoch):
	time_stamp = GENESIS_TIME_STAMP + epoch * SLOT_PER_EPOCH * SECOND_OF_SLOT
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_stamp))

	

