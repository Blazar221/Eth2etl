from entity import *
from constant import SLASHINGA_VLD, DEPOSIT


# Parse raw json from prysm api to attestion entity array
def json_to_attestation_array(json, slot):
	res = []
	for each in json:
		raw_data = each['data']
		item = attestation(slot, each['aggregationBits'], raw_data['slot'], raw_data['committeeIndex'], raw_data['beaconBlockRoot'], raw_data['source']['epoch'], raw_data['source']['root'], raw_data['target']['epoch'], raw_data['target']['root'], each['signature'])
		res.append(item)
	return res


def json_to_deposit_array(json, block_root):
	res = []
	for each in json:
		proof = each['proof']
		pub_key = each['data']['publicKey']
		withdraw_cred = each['data']['withdrawalCredentials']
		amount = each['data']['amount']
		amount = int(amount[:-9]) # Otherwise this number is too large to save
		dpst_sign = each['data']['signature']
		res.append(deposit(block_root, proof, pub_key, withdraw_cred, amount, dpst_sign))
	return res

		
def json_to_exiting_array(json, block_root):
	res = []
	for each in json:
		epoch = each['exit']['epoch']
		index = each['exit']['validatorIndex']
		sign = each['signature']
		res.append(exiting(block_root, epoch, index, sign))
	return res


def json_to_slashingp_array(json, block_root):
	res = []
	for each in json:
		slot1 = each['header1']['header']['slot']
		vld1 = each['header1']['header']['proposerIndex']
		parent_root1 = each['header1']['header']['parentRoot']
		state_root1 = each['header1']['header']['stateRoot']
		body_root1 = each['header1']['header']['bodyRoot']
		sign1 = each['header1']['signature']
		slot2 = each['header2']['header']['slot']
		vld1 = each['header2']['header']['proposerIndex']
		parent_root2 = each['header2']['header']['parentRoot']
		state_root2 = each['header2']['header']['stateRoot']
		body_root2 = each['header2']['header']['bodyRoot']
		sign2 = each['header2']['signature']
		res.append(slashingp(block_root, vld1, slot1, parent_root1, state_root1, body_root1, sign1, vld2, slot2, parent_root2, state_root2, body_root2, sign2))
	return res


def json_to_slashinga_array(json, block_root):
	res = []
	for each in json:
		indice1 = each['attestation1']['attestingIndices']
		slot1 = each['attestation1']['data']['slot']
		cmt_index1 = each['attestation1']['data']['committeeIndex']
		block_root1 = each['attestation1']['data']['beaconBlockRoot']
		src_epoch1 = each['attestation1']['data']['source']['epoch']
		src_root1 = each['attestation1']['data']['source']['root']
		trgt_epoch1 = each['attestation1']['data']['target']['epoch']
		trgt_root1 = each['attestation1']['data']['target']['root']
		sign1 = each['attestation1']['signature']
		indice2 = each['attestation2']['attestingIndices']
		slot2 = each['attestation2']['data']['slot']
		cmt_index2 = each['attestation2']['data']['committeeIndex']
		block_root2 = each['attestation2']['data']['beaconBlockRoot']
		src_epoch2 = each['attestation2']['data']['source']['epoch']
		src_root2 = each['attestation2']['data']['source']['root']
		trgt_epoch2 = each['attestation2']['data']['target']['epoch']
		trgt_root2 = each['attestation2']['data']['target']['root']
		sign2 = each['attestation2']['signature']
		res.append(slashinga(block_root, indice1, slot1, cmt_index1, block_root1, src_epoch1, src_root1, trgt_epoch1, trgt_root1, sign1, indice2, slot2, cmt_index2, block_root2, src_epoch2, src_root2, trgt_epoch2, trgt_root2, sign2))
	return res
	

# Parse raw json from prysm api to block array, and extract the attached data like deposit, exiting,
# slashing attesters and slashing proposers
def json_to_block_array(json):
	res = []
	for each in json['blockContainers']:
		block_root = each['blockRoot']
		block_outter = each['block']
		sign = block_outter['signature']
		block_inner = block_outter['block']
		slot = block_inner['slot']
		proposer_index = block_inner['proposerIndex']
		parent_root = block_inner['parentRoot']
		state_root = block_inner['stateRoot']
		randao_reveal = block_inner['body']['randaoReveal']
		dpst_root = block_inner['body']['eth1Data']['depositRoot']
		dpst_count = block_inner['body']['eth1Data']['depositCount']
		block_hash = block_inner['body']['eth1Data']['blockHash']
		grff = block_inner['body']['graffiti']
		deposits = []
		exitings = []
		slashinga_array = []
		slashingp_array = []
		attestation_array = json_to_attestation_array(block_inner['body']['attestations'], slot)
		if block_inner['body']['deposits']:
			deposits = json_to_deposit_array(block_inner['body']['deposits'], block_root)
		if block_inner['body']['voluntaryExits']:
			exitings = json_to_exiting_array(block_inner['body']['voluntaryExits'], block_root)
		if block_inner['body']['proposerSlashings']:
			slashingp_array = json_to_slashingp_array(block_inner['body']['proposerSlashings'], block_root)
		if block_inner['body']['attesterSlashings']:
			slashinga_array = json_to_slashinga_array(block_inner['body']['attesterSlashings'], block_root)
		b = block(slot, proposer_index, parent_root, state_root, randao_reveal, grff,sign, block_root, dpst_root, dpst_count, block_hash)
		res.append((b, deposits, exitings, slashinga_array, slashingp_array, attestation_array))
	return res


def json_to_validator_array(json):
	res = []
	for each in json['validatorList']:
		index = each['index']
		body = each['validator']
		pub_key = body['publicKey']
		withdraw_cred = body['withdrawalCredentials']
		e_balance = int(body['effectiveBalance'][:-5])
		slashed = body['slashed']
		act_eli_epoch = body['activationEligibilityEpoch']
		act_epoch = body['activationEpoch']
		exit_epoch = body['exitEpoch']
		withdraw_epoch = body['withdrawableEpoch']
		res.append(validator(index, pub_key, withdraw_cred, e_balance, slashed, act_eli_epoch, act_epoch, exit_epoch, withdraw_epoch))
	return res

		
def json_to_prop_and_cmt(json_array, timestamp):
	prop_dict = {}
	cmt= []
	for each in json_array:
		cmt.append(committee(each['attesterSlot'], each['committeeIndex'], each['beaconCommittees']))
		if each['proposerSlots']: # Sometimes a validator can be assigned as proposer twice in one epoch
			for slot in each['proposerSlots']:
				prop_dict[int(slot)] = each['validatorIndex']
	return prop_dict, cmt


def spawn_missed_block(slot, prop_index):
	return block(slot, prop_index)
