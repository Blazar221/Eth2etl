import api_service
import parse_service
import data_service
from head_info import *
from constant import DATA_BUFFER
	

def save_block_epoch(begin_epoch, end_epoch):
	blocks = []
	deposits = []
	exits = []
	slashingas = []
	slashingps = []
	attestations = []
	for i in range(begin_epoch, end_epoch + 1):
		json = api_service.block_epoch(i)
		res_array = parse_service.json_to_block_array(json)
		for block, deposit_array, exit_array, slashinga_array, slashingp_array, attestation_array in res_array:
			blocks.append(block)
			attestations.extend(attestation_array)
			if block.has_dpst:
				deposits.extend(deposit_array)
			if block.has_exit:
				exits.extend(exit_array)
			if block.has_sa:
				slashingas.extend(slashinga_array)
			if block.has_sp:
				slashingps.extend(slashingp_array)
		# Save all the data at once need too much memory space, so the proper way is to save the blocks epoch by epoch
		data_service.block_insert(blocks)
		data_service.attestation_insert(attestations)
		if deposits:
			data_service.deposit_insert(deposits)
		if exits:
			data_service.exit_insert(exits)
		if slashingas:
			data_service.slashinga_insert(slashingas)
		if slashingps:
			data_service.slashingp_insert(slashingps)
		# Clear all array and prepare for the next epoch
		blocks = []
		deposits = []
		exits = []
		slashingas = []
		slashingps = []
		attestations = []


# Probably the validators data of each epoch will have a large common part, thus save the data of head epoch is enough.
def save_vld_epoch(epoch):
	json = api_service.validators_epoch(epoch)
	res_array = parse_service.json_to_validator_array(json)
	if res_array:
		for i in range(0, len(res_array)/DATA_BUFFER):
			data_service.validator_insert(res_array[i*DATA_BUFFER, (i+1)*DATA_BUFFER])
	

def read_attestation(**kwargs):
	return parse_service.data_to_attestation_array(data_service.attestation_query(**kwargs))
	

def read_block(**kwargs):
	return parse_service.data_to_block_array(data_service.block_query(**kwargs))


def read_deposit(**kwargs):
	return parse_service.data_to_deposit_array(data_service.deposit_query(**kwargs))


def read_slashinga(**kwargs):
	return parse_service.data_to_slashinga_array(data_service.slashinga_query(**kwargs))


def read_slashingp(**kwargs):
	return parse_service.data_to_slashingp_array(data_service.slashingp_query(**kwargs))


# Get the current information about the beacon chain head and so on.
def get_current_head():
	raw_data = api_service.chainhead()
	head = headinfo(raw_data['headSlot'], raw_data['headEpoch'], raw_data['headBlockRoot'], raw_data['finalizedSlot'], raw_data['finalizedEpoch'], raw_data['finalizedBlockRoot'], raw_data['justifiedSlot'], raw_data['justifiedEpoch'], raw_data['justifiedBlockRoot'], raw_data['previousJustifiedSlot'], raw_data['previousJustifiedEpoch'], raw_data['previousJustifiedBlockRoot'])
	return head

