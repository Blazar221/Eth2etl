import api_service
import parse_service
import csv_service
import time_tool
from head_info import *


# TODO the miss block info is also needed
def request_block_epoch(begin_epoch, end_epoch):
	blocks = {}
	attestations = {}
	deposits = {}
	exitings = {}
	slashingas = {}
	slashingps = {}
	for i in range(begin_epoch, end_epoch + 1):
		json = api_service.block_epoch(i)
		res_array = parse_service.json_to_block_array(json)
		for block, deposit_array, exiting_array, slashinga_array, slashingp_array, attestation_array in res_array:
			day = time_tool.get_day_str(block.slot)
			if day in blocks:
				blocks[day].append(block)
			else:
				blocks[day] = [block]
			sub_key_name = '{}_{}'.format(day, block.block_root)
			attestations[sub_key_name] = attestation_array
			if deposit_array:
				deposits[sub_key_name] = deposits_array
			if exiting_array:
				exitings[sub_key_name] = exiting_array
			if slashinga_array:
				slashingas[sub_key_name] = slashinga_array
			if slashingp_array:
				slashingps[sub_key_name] = slashingp_array
	return blocks, attestations, deposits, exitings, slashingas, slashingps
			

# Probably the validators data of each epoch will have a large common part, thus save the data of head epoch is enough.
def request_vld_epoch(epoch):
	vld_array = []
	json = api_service.validators_epoch(epoch)
	while json['nextPageToken']:
		vld_array.extend(parse_service.json_to_validator_array(json))
		json = api_service.validators_epoch(epoch, pageToken = json['nextPageToken'])
	vld_array.extend(parse_service.json_to_validator_array(json))
	return vld_array


def save_attestation_csv(attes):
	data = []
	for each in attes:
		data.append(each.line())	
	csv_service.save_csv('attestation', data)


def save_blocks_csv(blocks):
	for key in blocks:
		data = []
		for block in blocks[key]:
			data.append(block.csv_line())
		csv_service.save_csv('block_'+key, data)


def save_deposit_csv(dpst):
	data = []
	proof_data = []
	for each in dpst:
		tuple = dpst.line()
		data.append(tuple[0], tuple[1], tuple[3], tuple[4], tuple[5], tuple[6])


# Get the current information about the beacon chain head and so on.
def get_current_head():
	raw_data = api_service.chainhead()
	head = headinfo(raw_data['headSlot'], raw_data['headEpoch'], raw_data['headBlockRoot'], raw_data['finalizedSlot'], raw_data['finalizedEpoch'], raw_data['finalizedBlockRoot'], raw_data['justifiedSlot'], raw_data['justifiedEpoch'], raw_data['justifiedBlockRoot'], raw_data['previousJustifiedSlot'], raw_data['previousJustifiedEpoch'], raw_data['previousJustifiedBlockRoot'])
	return head



