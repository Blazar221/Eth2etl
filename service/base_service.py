import api_service
import parse_service
import csv_service
from utils import encode_tool, time_tool
from head_info import *
from constant import SLOT_PER_EPOCH, CSV_NAME_MAP


# This method includes the retrieval of block data and committee data. 
#
# @return: Dicts of block data, block affiliated data and committee data. The key is the csv name identified standard. The value is the entity array. 
def request_block_epoch(begin_epoch, end_epoch):
	blocks = {}
	attestations = {}
	deposits = {}
	exitings = {}
	slashingas = {}
	slashingps = {}
	cmts = {}
	c = clock()
	for i in range(begin_epoch, end_epoch + 1):
		c.print_time()
		(prop_dict, cmt_array) = request_assignment_epoch(i)
		c.print_time()
		# Currently the committee use epoch to identify csv
		cmts[i] = cmt_array
		slot_head = i * SLOT_PER_EPOCH
		slot_end = slot_head + SLOT_PER_EPOCH		
		res_array = parse_service.json_to_block_array(api_service.block_epoch(i))
		c.print_time()		
		for block, deposit_array, exiting_array, slashinga_array, slashingp_array, attestation_array in res_array: 
			while block.slot > slot_head:
				add_missed_block(slot_head, prop_dict[slot_head], blocks)
				slot_head += 1	
			day = time_tool.get_day_str(block.slot)
			if day in blocks:
				blocks[day].append(block)
			else:
				blocks[day] = [block]
			sub_key_name = '{}_{}'.format(day, encode_tool.safe_url_base64(block.block_root))
			attestations[sub_key_name] = attestation_array
			if deposit_array:
				deposits[sub_key_name] = deposits_array
			if exiting_array:
				exitings[sub_key_name] = exiting_array
			if slashinga_array:
				slashingas[sub_key_name] = slashinga_array
			if slashingp_array:
				slashingps[sub_key_name] = slashingp_array
			slot_head += 1
			c.print_time()
		while slot_head < slot_end:
			add_missed_slot(slot_head, blocks)
			slot_head += 1
	return blocks, attestations, deposits, exitings, slashingas, slashingps, cmts


# This method can retrieve both committee and missing block
def request_assignment_epoch(epoch):		
	assignment = []
	info = api_service.validators_assignments_epoch(epoch)
	while info['nextPageToken']:
		assignment.extend(info['assignments'])
		info = api_service.validators_assignments_epoch(epoch, pageToken = info['nextPageToken'])
	assignment.extend(info['assignments'])
	epoch_timestamp = time_tool.get_timestamp_epoch(epoch)
	prop_dict, cmt = parse_service.json_to_prop_and_cmt(assignment, epoch_timestamp)
	return prop_dict, cmt


# Probably the validators data of each epoch will have a large common part, thus save the data of head epoch is enough.
def request_vld_epoch(epoch):
	vld_array = []
	json = api_service.validators_epoch(epoch)
	while json['nextPageToken']:
		vld_array.extend(parse_service.json_to_validator_array(json))
		json = api_service.validators_epoch(epoch, pageToken = json['nextPageToken'])
	vld_array.extend(parse_service.json_to_validator_array(json))
	return vld_array


def save_csv(data_dict, name_key):
	for key in data_dict:
		data = []
		for each in data_dict[key]:
			data.append(each.csv_format())
		csv_service.save_csv('{}{}'.format(CSV_NAME_MAP[name_key], key), data)


def add_missed_block(slot, prop, blocks):
	day = time_tool.get_day_str(slot)
	missed_block = parse_service.spawn_missed_block(slot, prop)
	if day in blocks:
		blocks[day].append(missed_block)
	else:
		blocks[day] = [missed_block]

	
# Get the current information about the beacon chain head and so on.
def get_current_head():
	raw_data = api_service.chainhead()
	head = headinfo(raw_data['headSlot'], raw_data['headEpoch'], raw_data['headBlockRoot'], raw_data['finalizedSlot'], raw_data['finalizedEpoch'], raw_data['finalizedBlockRoot'], raw_data['justifiedSlot'], raw_data['justifiedEpoch'], raw_data['justifiedBlockRoot'], raw_data['previousJustifiedSlot'], raw_data['previousJustifiedEpoch'], raw_data['previousJustifiedBlockRoot'])
	return head



