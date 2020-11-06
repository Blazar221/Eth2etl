import api_service
import parse_service
import data_service
import csv_service
from head_info import *
from constant import DATA_BUFFER


def request_block_epoch(begin_epoch, end_epoch):
	blocks = []
	deposits = []
	exitings = []
	slashingas = []
	slashingps = []
	attestations = []
	for i in range(begin_epoch, end_epoch + 1):
		json = api_service.block_epoch(i)
		res_array = parse_service.json_to_block_array(json)
		for block, deposit_array, exiting_array, slashinga_array, slashingp_array, attestation_array in res_array:
			blocks.append(block)
			attestations.extend(attestation_array)
			if block.has_dpst:
				deposits.extend(deposit_array)
			if block.has_exiting:
				exitings.extend(exiting_array)
			if block.has_sa:
				slashingas.extend(slashinga_array)
			if block.has_sp:
				slashingps.extend(slashingp_array)
	return blocks, deposits, exitings, slashingas, slashingps, attestations


# Probably the validators data of each epoch will have a large common part, thus save the data of head epoch is enough.
def request_vld_epoch(epoch):
	vld_array = []
	json = api_service.validators_epoch(epoch)
	while json['nextPageToken']:
		vld_array.extend(parse_service.json_to_validator_array(json))
		json = api_service.validators_epoch(epoch, pageToken = json['nextPageToken'])
	vld_array.extend(parse_service.json_to_validator_array(json))
	return vld_array


def save_attestation_db(atte):
	if atte:
		for i in range(0, int(len(atte)/DATA_BUFFER)+1):
			data_service.attestation_insert(atte[i*DATA_BUFFER:(i+1)*DATA_BUFFER])

		
def save_block_db(block):
	if block:
		for i in range(0, int(len(block)/DATA_BUFFER)+1):
			data_service.block_insert(block[i*DATA_BUFFER:(i+1)*DATA_BUFFER])


def save_deposit_db(dpst):
	if dpst:
		for i in range(0, int(len(dpst)/DATA_BUFFER)+1):
			data_service.deposit_insert(dpst[i*DATA_BUFFER:(i+1)*DATA_BUFFER])


def save_exiting_db(ex):
	if ex:
		for i in range(0, int(len(ex)/DATA_BUFFER)+1):
			data_service.exiting_insert(ex[i*DATA_BUFFER:(i+1)*DATA_BUFFER])


def save_slashinga_db(sa):
	if sa:
		for i in range(0, int(len(sa)/DATA_BUFFER)+1):
			data_service.slashinga_insert(sa[i*DATA_BUFFER:(i+1)*DATA_BUFFER])


def save_slashingp_db(sp):
	if sp:
		for i in range(0, int(len(sp)/DATA_BUFFER)+1):
			data_service.slashingp_insert(sp[i*DATA_BUFFER:(i+1)*DATA_BUFFER])


def save_vld_db(vld):
	if vld:
		for i in range(0, int(len(vld)/DATA_BUFFER)+1):
			data_service.validator_insert(vld[i*DATA_BUFFER:(i+1)*DATA_BUFFER])


def save_attestation_csv(attes):
	data = []
	for each in attes:
		data.append(each.line())	
	csv_service.save_csv('attestation', data)


def save_block_csv(block):
	data = []
	for each in block:
		data.append(each.line())
	csv_service.save_csv('block', data)


def save_deposit(dpst):
	data = []
	proof_data = []
	for each in dpst:
		tuple = dpst.line()
		data.append(tuple[0], tuple[1], tuple[3], tuple[4], tuple[5], tuple[6])
		

def read_attestation_db(**kwargs):
	return parse_service.data_to_attestation_array(data_service.attestation_query(**kwargs))
	

def read_block_db(**kwargs):
	return parse_service.data_to_block_array(data_service.block_query(**kwargs))


def read_deposit_db(**kwargs):
	return parse_service.data_to_deposit_array(data_service.deposit_query(**kwargs))


def read_slashinga_db(**kwargs):
	return parse_service.data_to_slashinga_array(data_service.slashinga_query(**kwargs))


def read_slashingp_db(**kwargs):
	return parse_service.data_to_slashingp_array(data_service.slashingp_query(**kwargs))


def read_validator_db(**kwargs):
	return parse_service.data_to_validator_array(data_service.validator_query(**kwargs))


# Get the current information about the beacon chain head and so on.
def get_current_head():
	raw_data = api_service.chainhead()
	head = headinfo(raw_data['headSlot'], raw_data['headEpoch'], raw_data['headBlockRoot'], raw_data['finalizedSlot'], raw_data['finalizedEpoch'], raw_data['finalizedBlockRoot'], raw_data['justifiedSlot'], raw_data['justifiedEpoch'], raw_data['justifiedBlockRoot'], raw_data['previousJustifiedSlot'], raw_data['previousJustifiedEpoch'], raw_data['previousJustifiedBlockRoot'])
	return head

