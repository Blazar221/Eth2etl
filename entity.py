from encode import db_parse as parse

class attestation:
	aggr_bits = ''
	slot = 0
	cmt_index = 0
	block_root = ''
	src_epoch = 0
	src_root = ''
	trgt_epoch = 0
	trgt_root = ''
	sign = ''


	def __init__(self, aggr_bits, slot, cmt_index, block_root, src_epoch, src_block, trgt_epoch, trgt_block, sign):
		self.aggr_bits = parse(aggr_bits)
		self.slot = slot
		self.cmt_index = cmt_index
		self.block_root = parse(block_root)
		self.src_epoch = src_epoch
		self.src_block = parse(src_block)
		self.trgt_epoch = trgt_epoch
		self.trgt_block = parse(trgt_block)
		self.sign = sign


	def __repr__(self):
		return 'aggr_bits={}, slot={}, cmt_index={}, block_root={}, src_epoch={}, src_root={}, trgt_epoch={}, trgt_root={}, sign={}'.format(self.aggr_bits, self.slot, self.cmt_index, self.block_root, self.src_epoch, self.src_block, self.trgt_epoch, self.trgt_block, self.sign)


class block:
	slot = 0
	prop_index = 0
	parent_root = 0
	state_root = 0
	randao_reveal = ''
	grff = ''
	sign = ''
	block_root = ''
	dpst_root = ''
	dpst_count = 0
	block_hash = ''
	has_dpst = False
	has_exit = False
	has_sp = False
	has_sa = False


	def __init__(self, slot, prop_index, parent_root, state_root, randao_reveal, grff, sign, block_root, dpst_root, dpst_count, block_hash, has_dpst, has_exit, has_sa, has_sp):
		self.slot = slot
		self.prop_index = prop_index
		self.parent_root = parse(parent_root)
		self.state_root = parse(state_root)
		self.randao_reveal = randao_reveal
		self.grff = parse(grff)
		self.sign = sign
		self.block_root = parse(block_root)
		self.dpst_root = parse(dpst_root)
		self.dpst_count = dpst_count
		self.block_hash = parse(block_hash)
		self.has_dpst = has_dpst
		self.has_exit = has_exit
		self.has_sa = has_sa
		self.has_sp = has_sp


	def __repr__(self):
		return 'slot={},prop_index={},parent_root={},state_root={},randao_reveal={},grff={}, sign={}, block_root={},dpst_root={},dpst_count={},block_hash={},has_dpst={},has_exit={},has_sa={},has_sp={}'.format(self.slot, self.prop_index, self.parent_root, self.state_root, self.randao_reveal, self.grff, self.sign, self.block_root, self.dpst_root, self.dpst_count, self.block_hash, self.has_dpst, self.has_exit, self.has_sa, self.has_sp)


class deposit:
	slot = 0
	block_root = ''
	proof = []
	pub_key = ''
	withdraw_cred = ''
	amount = 0
	sign = ''


	def __init__(self, slot, block_root, proof, pub_key, withdraw_cred, amount, sign):
		self.slot = slot
		self.block_root = parse(block_root)
		self.proof = [parse(x) for x in proof]
		self.pub_key = pub_key
		self.withdraw_cred = parse(withdraw_cred)
		self.amount = amount
		self.sign = sign


	def __repr__(self):
		return 'slot={}, block_root={},proof={},pub_key={},withdraw_cred={},amount={},sign={}'.format(self.slot, self.block_root, self.proof, self.pub_key, self.withdraw_cred, self.amount, self.sign)
	

class exit:
	slot = 0
	block_root = ''
	exit_epoch = 0
	validator_index = 0
	sign = ''


	def __init__(self, slot, block_root, exit_epoch, validator_index, sign):
		self.slot = slot
		self.block_root = block_root
		self.exit_epoch = exit_epoch
		self.validator_index = validator_index
		self.sign = sign


	def __repr__(self):
		return 'slot={}, block_root={},exit_epoch={},validator_index={},sign={}'.format(self.slot, self.block_root, self.exit_epoch, self.validator_index, self.sign)


class slashinga:
	slot = 0
	block_root = ''
	indice1 = []
	slot1 = 0
	cmt_index1 = 0
	block_root1 = ''
	src_epoch1 = 0
	src_root1 = ''
	trgt_epoch1 = 0
	trgt_root1 = ''
	sign1 = ''
	indice2 = []
	slot2 = 0
	cmt_index2 = 0
	block_root2 = ''
	src_epoch2 = 0
	src_root2 = ''
	trgt_epoch2 = 0
	trgt_root2 = ''
	sign2 = ''


	def __init__(self, slot, block_root, indice1, slot1, cmt_index1, block_root1, src_epoch1, src_root1, trgt_epoch1, trgt_root1, sign1, indice2, slot2, cmt_index2, block_root2, src_epoch2, src_root2, trgt_epoch2, trgt_root2, sign2):
		self.slot = slot
		self.block_root = parse(block_root)
		self.indice1 = indice1
		self.slot1 = slot1
		self.cmt_index1 = cmt_index1
		self.block_root1 = parse(block_root1)
		self.src_epoch1 = src_epoch1
		self.src_root1 = parse(src_root1)
		self.trgt_epoch1 = trgt_epoch1
		self.trgt_root1 = parse(trgt_root1)
		self.sign1 = sign1
		self.indice2 = indice2
		self.slot2 = slot2
		self.cmt_index2 = cmt_index2
		self.block_root2 = parse(block_root2)
		self.src_epoch2 = src_epoch2
		self.src_root2 = parse(src_root2)
		self.trgt_epoch2 = trgt_epoch2
		self.trgt_root2 = parse(trgt_root2)
		self.sign2 = sign2


	def __repr__(self):
		return 'slot={},block_root={},indice1={},slot1={}, cmt_index1={},block_root1={},src_epoch1={},src_root1={},trgt_epoch1={},trgt_root1={},sign1={},indice2={},slot2={}, cmt_index2={},block_root2={},src_epoch2={},src_root2={},trgt_epoch2={},trgt_root2={},sign2={}'.format(self.slot,self.block_root,self.indice1,self.slot1,self.cmt_index1,self.block_root1,self.src_epoch1,self.src_root1,self.trgt_epoch1,self.sign1,self.indice2,self.slot2,self.cmt_index2,self.block_root2,self.src_epoch2,self.src_root2,
self.trgt_epoch2,self.sign2)


class slashingp:
	slot = 0
	block_root = ''
	vld_index = 0
	slot1 = 0
	parent_root1 = ''
	state_root1 = ''
	body_root1 = ''
	sign1 = ''
	slot2 = 0
	parent_root2 = ''
	state_root2 = ''
	body_root2 = ''
	sign2 = ''


	def __init__(self, slot, block_root, vld_index, slot1, parent_root1, state_root1, body_root1, sign1, slot2, parent_root2, state_root2, body_root2, sign2):
		self.slot = slot
		self.block_root = parse(block_root)
		self.vld_index = vld_index
		self.slot1 = slot1
		self.parent_root1 = parse(parent_root1)
		self.state_root1 = parse(state_root1)
		self.body_root1 = parse(body_root1)
		self.sign1 = sign1
		self.slot2 = slot2
		self.parent_root2 = parse(parent_root2)
		self.state_root2 = parse(state_root2)
		self.body_root2 = parse(body_root2)
		self.sign2 = sign2


	def __repr__(self):
		return 'slot={},block_root={},vld_index={},slot1={},parent_root1={},state_root1={},body_root1={},sign1={},slot2={},index2={},parent_root2={},state_root2={},body_root2={},sign2={}'.format(self.slot, self.block_root, self.vld_index, self.slot1, self.parent_root1, self.state_root1, self.body_root1, self.sign1, self.slot2, self.parent_root2, self.state_root2, self.body_root2, self.sign2)

	
	
	
		
