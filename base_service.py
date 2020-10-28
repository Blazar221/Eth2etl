from entity import *


# Parse raw json from prysm api to attestion entity array
def json_to_attestation_array(json):
	res = []
	for each in json:
		raw_data = each['data']
		item = attestation(each['aggregationBits'], raw_data['slot'], raw_data['committeeIndex'], raw_data['beaconBlockRoot'], raw_data['source']['epoch'], raw_data['source']['root'], raw_data['target']['epoch'], raw_data['target']['root'], each['signature'])
		res.append(item)
	return res


def json_to_deposit_array(json):
	res = []
	for each in json:
		proof = each['proof']
		pub_key = each['data']['publicKey']
		withdraw_cred = each['data']['withdrawalCredentials']
		amount = each['data']['amount']
		dpst_sign = each['data']['signature']
		res.append(deposit(slot, block_root, proof, pub_key, withdraw_cred, amount, dpst_sign))
	return res


# Parse raw json from prysm api to block array, and extract the attached data like deposit, exiting, slashing attesters and slashing proposers
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
		has_dpst = False
		deposits = []
		has_exit = False
		exits = []
		has_sa = False
		slashinga_array = []
		has_sp = False
		slashingp_array = []
		attestation_array = json_to_attestation_array(block_inner['body']['attestations'])
		if block_inner['body']['deposits']:
			has_dpst = True
			deposits = json_to_deposit_array(block_inner['body']['deposits'])
		if block_inner['body']['voluntaryExits']:
			has_exit = True
			for each_exit in block_inner['body']['voluntaryExits']:
				exit_epoch = each_exit['exit']['epoch']
				exit_index = each_exit['exit']['validatorIndex']
				exit_sign = each_exit['signature']
				exits.append(exit(slot, block_root, exit_epoch, exit_index, exit_sign))
		if block_inner['body']['proposerSlashings']:
			has_sp = True
			for each_slashingp in block_inner['body']['proposerSlashings']:
				slot1 = each_slashingp['header1']['header']['slot']
				vld_index = each_slashingp['header1']['header']['proposerIndex']
				parent_root1 = each_slashingp['header1']['header']['parentRoot']
				state_root1 = each_slashingp['header1']['header']['stateRoot']
				body_root1 = each_slashingp['header1']['header']['bodyRoot']
				sign1 = each_slashingp['header1']['signature']
				slot2 = each_slashingp['header2']['header']['slot']
				parent_root2 = each_slashingp['header2']['header']['parentRoot']
				state_root2 = each_slashingp['header2']['header']['stateRoot']
				body_root2 = each_slashingp['header2']['header']['bodyRoot']
				sign2 = each_slashingp['header2']['signature']
				slashingp_array.append(slashingp(slot, block_root, vld_index, slot1, parent_root1, state_root1, body_root1, sign1, slot2, parent_root2, state_root2, body_root2, sign2))
		if block_inner['body']['attesterSlashings']:
			has_sa = True
			for each_slashinga in block_inner['body']['attesterSlashings']:
				indice1 = each_slashinga['attestation1']['attestingIndices']
				slot1 = each_slashinga['attestation1']['data']['slot']
				cmt_index1 = each_slashinga['attestation1']['data']['committeeIndex']
				block_root1 = each_slashinga['attestation1']['data']['beaconBlockRoot']
				src_epoch1 = each_slashinga['attestation1']['data']['source']['epoch']
				src_root1 = each_slashinga['attestation1']['data']['source']['root']
				trgt_epoch1 = each_slashinga['attestation1']['data']['target']['epoch']
				trgt_root1 = each_slashinga['attestation1']['data']['target']['root']
				sign1 = each_slashinga['attestation1']['signature']
				indice2 = each_slashinga['attestation2']['attestingIndices']
				slot2 = each_slashinga['attestation2']['data']['slot']
				cmt_index2 = each_slashinga['attestation2']['data']['committeeIndex']
				block_root2 = each_slashinga['attestation2']['data']['beaconBlockRoot']
				src_epoch2 = each_slashinga['attestation2']['data']['source']['epoch']
				src_root2 = each_slashinga['attestation2']['data']['source']['root']
				trgt_epoch2 = each_slashinga['attestation2']['data']['target']['epoch']
				trgt_root2 = each_slashinga['attestation2']['data']['target']['root']
				sign2 = each_slashinga['attestation2']['signature']
				slashinga_array.append(slashinga(slot, block_root, indice1, slot1, cmt_index1, block_root1, src_epoch1, src_root1, trgt_epoch1, trgt_root1, sign1, indice2, slot2, cmt_index2, block_root2, src_epoch2, src_root2, trgt_epoch2, trgt_root2, sign2))
		b = block(slot, proposer_index, parent_root, state_root, randao_reveal, grff,sign, block_root, dpst_root, dpst_count, block_hash, has_dpst, has_exit, has_sa, has_sp)
		res.append((b, deposits, exits, slashinga_array, slashingp_array, attestation_array))
	return res
		
