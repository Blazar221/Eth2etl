import time_tool
from constant import SLOT_PER_EPOCH

class attestation:
	def __init__(self, inclusion_slot, aggr_bits, slot, cmt_index, block_root, src_epoch, src_block, trgt_epoch, trgt_block, sign):
		self.inclusion_slot = inclusion_slot
		self.aggr_bits = aggr_bits
		self.slot = slot
		self.cmt_index = cmt_index
		self.block_root = block_root
		self.src_epoch = src_epoch
		self.src_block = src_block
		self.trgt_epoch = trgt_epoch
		self.trgt_block = trgt_block
		self.sign = sign


	def __repr__(self):
		return 'inclusion={}, aggr_bits={}, slot={}, cmt_index={}, block_root={}, src_epoch={}, src_root={}, trgt_epoch={}, trgt_root={}, sign={}'.format(self.inclusion_slot, self.aggr_bits, self.slot, self.cmt_index, self.block_root, self.src_epoch, self.src_block, self.trgt_epoch, self.trgt_block, self.sign)

	
	def line(self):
		return (self.inclusion_slot, self.aggr_bits, self.slot, self.cmt_index, self.block_root, self.src_epoch, self.src_block, self.trgt_epoch, self.trgt_block, self.sign)


class block:
	def __init__(self, slot, prop_index, parent_root, state_root, randao_reveal, grff, sign, block_root, dpst_root, dpst_count, block_hash):
		self.slot = int(slot)
		self.prop_index = prop_index
		self.parent_root = parent_root
		self.state_root = state_root
		self.randao_reveal = randao_reveal
		self.grff = grff
		self.sign = sign
		self.block_root = block_root
		self.dpst_root = dpst_root
		self.dpst_count = dpst_count
		self.block_hash = block_hash


	def __repr__(self):
		return 'slot={},prop_index={},parent_root={},state_root={},randao_reveal={},grff={}, sign={}, block_root={},dpst_root={},dpst_count={},block_hash={}'.format(self.slot, self.prop_index, self.parent_root, self.state_root, self.randao_reveal, self.grff, self.sign, self.block_root, self.dpst_root, self.dpst_count, self.block_hash)
	
	
	def csv_line(self):
		return (self.slot, int(self.slot/SLOT_PER_EPOCH), time_tool.get_timestamp(self.slot), self.prop_index, False, self.block_root, self.parent_root, self.state_root, self.randao_reveal, self.grff, self.block_hash, self.dpst_root, self.dpst_count, self.sign)


class deposit:
	def __init__(self, block_root, proof, pub_key, withdraw_cred, amount, sign):
		self.block_root = block_root
		self.proof = proof
		self.pub_key = pub_key
		self.withdraw_cred = withdraw_cred
		self.amount = amount
		self.sign = sign


	def __repr__(self):
		return 'block_root={},proof={},pub_key={},withdraw_cred={},amount={},sign={}'.format(self.block_root, self.proof, self.pub_key, self.withdraw_cred, self.amount, self.sign)
	

	def line(self):
		return (self.block_root, self.proof, self.pub_key, self.withdraw_cred, self.amount, self.sign)


class exiting:
	def __init__(self, block_root, exit_epoch, vld_index, sign):
		self.block_root = block_root
		self.exit_epoch = exit_epoch
		self.vld_index = vld_index
		self.sign = sign


	def __repr__(self):
		return 'block_root={},exit_epoch={},validator_index={},sign={}'.format(self.block_root, self.exit_epoch, self.validator_index, self.sign)

	
	def line(self):
		return (self.block_root, self.exit_epoch, self.validator_index, self.sign)


class slashinga:
	def __init__(self, block_root, indice1, slot1, cmt_index1, block_root1, src_epoch1, src_root1, trgt_epoch1, trgt_root1, sign1, indice2, slot2, cmt_index2, block_root2, src_epoch2, src_root2, trgt_epoch2, trgt_root2, sign2):
		self.block_root = block_root
		self.indice1 = indice1
		self.slot1 = slot1
		self.cmt_index1 = cmt_index1
		self.block_root1 = block_root1
		self.src_epoch1 = src_epoch1
		self.src_root1 = src_root1
		self.trgt_epoch1 = trgt_epoch1
		self.trgt_root1 = trgt_root1
		self.sign1 = sign1
		self.indice2 = indice2
		self.slot2 = slot2
		self.cmt_index2 = cmt_index2
		self.block_root2 = block_root2
		self.src_epoch2 = src_epoch2
		self.src_root2 = src_root2
		self.trgt_epoch2 = trgt_epoch2
		self.trgt_root2 = trgt_root2
		self.sign2 = sign2


	def __repr__(self):
		return 'block_root={},indice1={},slot1={}, cmt_index1={},block_root1={},src_epoch1={},src_root1={},trgt_epoch1={},trgt_root1={},sign1={},indice2={},slot2={}, cmt_index2={},block_root2={},src_epoch2={},src_root2={},trgt_epoch2={},trgt_root2={},sign2={}'.format(self.block_root, self.indice1, self.slot1, self.cmt_index1, self.block_root1, self.src_epoch1, self.src_root1, self.trgt_epoch1, self.trgt_root1, self.sign1, self.indice2, self.slot2, self.cmt_index2, self.block_root2, self.src_epoch2, self.src_root2,self.trgt_epoch2, self.trgt_root2, self.sign2)


	def line(self):
		return (self.block_root, self.indice1, self.slot1, self.cmt_index1, self.block_root1, self.src_epoch1, self.src_root1, self.trgt_epoch1, self.trgt_root1, self.sign1, self.indice2, self.slot2, self.cmt_index2, self.block_root2, self.src_epoch2, self.src_root2,self.trgt_epoch2, self.trgt_root2, self.sign2)


class slashingp:
	def __init__(self, block_root, vld_index, slot1, parent_root1, state_root1, body_root1, sign1, slot2, parent_root2, state_root2, body_root2, sign2):
		self.block_root = block_root
		self.vld_index = vld_index
		self.slot1 = slot1
		self.parent_root1 = parent_root1
		self.state_root1 = state_root1
		self.body_root1 = body_root1
		self.sign1 = sign1
		self.slot2 = slot2
		self.parent_root2 = parent_root2
		self.state_root2 = state_root2
		self.body_root2 = body_root2
		self.sign2 = sign2


	def __repr__(self):
		return 'block_root={},vld_index={},slot1={},parent_root1={},state_root1={},body_root1={},sign1={},slot2={},parent_root2={},state_root2={},body_root2={},sign2={}'.format(self.block_root, self.vld_index, self.slot1, self.parent_root1, self.state_root1, self.body_root1, self.sign1, self.slot2, self.parent_root2, self.state_root2, self.body_root2, self.sign2)

	
	def line(self):
		return (self.block_root, self.vld_index, self.slot1, self.parent_root1, self.state_root1, self.body_root1, self.sign1, self.slot2, self.parent_root2, self.state_root2, self.body_root2, self.sign2)


class validator:
	def __init__(self, index, pub_key, withdraw_cred, e_balance, slashed, act_eli_epoch, act_epoch, exit_epoch, withdraw_epoch):
		self.index = index
		self.pub_key = pub_key
		self.withdraw_cred = withdraw_cred
		self.e_balance = e_balance
		self.slashed = slashed
		self.act_eli_epoch = act_eli_epoch
		self.act_epoch = act_epoch
		self.exit_epoch = exit_epoch
		self.withdraw_epoch = withdraw_epoch


	def __repr__(self):
		return 'index={},pub_key={},withdraw_cred={},e_balance={},slashed={},act_eli_epoch={},act_epoch={},exit_epoch={},withdraw_epoch={}'.format(self.index, self.pub_key, self.withdraw_cred, self.e_balance, self.slashed, self.act_eli_epoch, self.act_epoch, self.exit_epoch, self.withdraw_epoch)
	
	
	def line(self):
		return (self.index, self.pub_key, self.withdraw_cred, self.e_balance, self.slashed, self.act_eli_epoch, self.act_epoch, self.exit_epoch, self.withdraw_epoch)
		
