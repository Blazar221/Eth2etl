from entity import *


# Parse raw json from prysm api to attestion entity array
def json_to_attestation_array(json):
	res = []
	for each in json['attestations']:
		raw_data = each['data']
		item = attestation(each['aggregationBits'], raw_data['slot'], raw_data['committeeIndex'], raw_data['beaconBlockRoot'], raw_data['source']['epoch'], raw_data['source']['root'], raw_data['target']['epoch'], raw_data['target']['root'], each['signature'])
		res.append(item)
	return res


# Parse raw json from prysm api to block array, and extract the attached data like deposit, exiting, slashing attesters and slashing proposers
def json_to_block_array(json):
	res = []
	for each in json['blockContainers']:
		block_root = each['blockRoot']
		block_outter = each['block']
		sign = block_outter['signature']
		block_inner = block['block']
		slot = block_inner['slot']
		proposer_index = block_inner['proposerIndex']
		parent_root = block_inner['parent_root']
		state_root = block_inner['state_root']
		randao_reveal = block_inner['body']['randao_reveal']
		dpst_root = block_inner['body']['eth1data']['depositRoot']
		dpst_count = block_inner['body']['eth1data']['depositCount']
		block_hash = block_inner['body']['eth1data']['blockHash']
		grff = block_inner['graffiti']
		has_deposit = False
		deposits = []
		has_exit = False
		exits = []
		has_slashinga = False
		slashingas = []
		has_slashingp = False
		slashingps = []
		if block_inner['body']['deposits']:
			has_deposit = True
			for deposit in block_inner['body']['deposits']:
				proof = deposit['proof']
				pub_key = deposit['data']['publicKey']
				withdraw_cred = deposit['data']['withdrawCredentials']
				amount = deposit['data']['amount']
				dpst_sign = deposit['data']['signature']
				deposits.append(deposit(slot, block_root, proof, pub_key, withdraw_cred, amount, dpst_sign)
		if block_inner['body']['voluntaryExits']:
			has_exit = True
			for exit in block['inner']['voluntaryExits']:
				exit_epoch = exit['exit']['epoch']
				exit_index = exit['exit']['validatorIndex']
				exit_sign = exit['signature']
				exits.append(exit(slot, block_root, exit_epoch, exit_index, exit_sign)
		if block_inner['body']['proposerSlashings']:
			has_slashingp = True
			for slashingp in block['body']['proposerSlashings']:
				slot1 = slashingp['header1']['header']['slot']
				index1 = slashingp['header1']['header']['proposerIndex']
				parent_root1 = slashingp['header1']['header']['parentRoot']
				state_root1 = slashingp['header1']['header']['stateRoot']
				body_root1 = slashingp['header1']['header']['bodyRoot']
				sign1 = slashingsp['header1']['signature']
				slot2 = slashingp['header2']['header']['slot']
				index2 = slashingp['header2']['header']['proposerIndex']
				parent_root2 = slashingp['header2']['header']['parentRoot']
				state_root2 = slashingp['header2']['header']['stateRoot']
				body_root2 = slashingp['header2']['header']['bodyRoot']
				sign2 = slashingsp['header2']['signature']
				slashingps.append(slashingp(slot, block_root, slot1, index1, parent_root1, state_root1, body_root1, sign1, slot2, index2, parent_root2, state_root2, body_root2, sign2)
		if block_inner['body']['attesterSlashings']:
			has_slashinga = True
			for slashinga in block['body']['attesterSlashings']:
				indice1 = slashinga['attestation1']['attestingIndices']
				slot1 = slashinga['attestation1']['data']['slot']
				cmt_index1 = slashinga['attestation1']['data']['committeeIndex']
				block_root1 = slashinga['attestation1']['data']['beaconBlockRoot']
				src_epoch1 = slashinga['attestation1']['data']['source']['epoch']
				src_root1 = slashinga['attestation1']['data']['source']['root']
				trgt_epoch1 = slashinga['attestation1']['data']['target']['epoch']
				trgt_root1 = slashinga['attestation1']['data']['target']['root']
				sign1 = slashing['attestation1']['signature']
				indice2 = slashinga['attestation2']['attestingIndices']
				slot2 = slashinga['attestation2']['data']['slot']
				cmt_index2 = slashinga['attestation2']['data']['committeeIndex']
				block_root2 = slashinga['attestation2']['data']['beaconBlockRoot']
				src_epoch2 = slashinga['attestation2']['data']['source']['epoch']
				src_root2 = slashinga['attestation2']['data']['source']['root']
				trgt_epoch2 = slashinga['attestation2']['data']['target']['epoch']
				trgt_root2 = slashinga['attestation2']['data']['target']['root']
				sign2 = slashing['attestation2']['signature']
				slashinga.append(slashinga(slot, block_root, indice1, slot1, cmt_index1, block_root1, src_epoch1, src_root1, a1_trgt_ecoch, trgt_root1, sign1, indice2, slot2, cmt_index2, block_root2, src_epoch2, src_root2, a2_trgt_ecoch, trgt_root2, sign2)
		b = block(slot, proposer_index, parent_root, state_root, randao_reveal, grff,sign, block_root, dpst_root, dpst_count, block_hash, has_dpst, has_exit, has_slashinga, has_slashingp)
		res.append((b, deposits, exits, slashinga, slashingp))
	return res
		
