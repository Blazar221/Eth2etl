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
		return 'aggr_bits={}, slot={}, cmt_index={}, block_root={}, src_epoch={}, src_root={}, trgt_epoch={}, trgt_root={}, sign={}'.format(self.aggr_bits, self.slot, self.cmt_index, self.block_root, self.src_epoch, self.src_block, self.trgt_epoch, self.trgt_block, self.sign)


class block:
	slot = 0
	proposer_index = 0
	parent_root = 0
	state_root = 0
	randao_reveal = ''
	dpst_root = ''
	dpst_count = 0
	block_hash = ''
	grff = ''
	sign = ''
	block_root = ''
	def __init__(self, slot, proposer_index, parent_root, state_root, randao_reveal, dpst_root, dpst_count, block_hash, grff,sign, block_root):
		self.slot = slot
		self.proposer_index = proposer_index
		self.parent_root = parent_root
		self.state_root =state_root
		self.randao_reveal = randao_reveal
		self.dpst_root = dpst_root
		self.dpst_count = dpst_count
		self.block_hash = block_hash
		self.grff = grff
		self.sign = sign
		self.block_root = block_root


class slashing_a:
	slot = 0
	a1_indice = 0
	a1_slot = 0
	a1_cmt_index = 0
	a1_block_root = ''
	a1_src_epoch = 0
	a1_src_root = ''
	a1_trgt_epoch = 0
	a1_trgt_root = ''
	a1_sign = ''
	a2_indice = 0
	a2_slot = 0
	a2_cmt_index = 0
	a2_block_root = ''
	a2_src_epoch = 0
	a2_src_root = ''
	a2_trgt_epoch = 0
	a2_trgt_root = ''
	a2_sign = ''
	def __init__(self, slot, a1_indice, a1_slot, a1_cmt_index, a1_block_root, a1_src_epoch, a1_src_root, a1_trgt_ecoch, a1_trgt_root, a1_sign, a2_indice, a2_slot, a2_cmt_index, a2_block_root, a2_src_epoch, a2_src_root, a2_trgt_ecoch, a2_trgt_root, a2_sign):
			self.slot = slot
			self.a1_indice = a1_indice
			self.a1_slot = a1_slot
			self.a1_cmt_index = a1_cmt_index
			self.a1_block_root = a1_block_root
			self.a1_src_epoch = a1_src_epoch
			self.a1_src_root = a1_src_root
			self.a1_trgt_epoch = a1_trgt_epoch
			self.a1_trgt_root = a1_trgt_root
			self.a1_sign = a1_sign
			self.a2_indice = a2_indice
			self.a2_slot = a2_slot
			self.a2_cmt_index = a2_cmt_index
			self.a2_block_root = a2_block_root
			self.a2_src_epoch = a2_src_epoch
			self.a2_src_root = a2_src_root
			self.a2_trgt_epoch = a2_trgt_epoch
			self.a2_trgt_root = a2_trgt_root
			self.a2_sign = a2_sign


class slashing_p:
	slot = 0
	validator_index = 0
	h1_slot = 0
	h1_parent_root = ''
	h1_state_root = ''
	h1_body_root = ''
	h1_sign = ''
	h2_slot = 0
	h2_parent_root = ''
	h2_state_root = ''
	h2_body_root = ''
	h2_sign = ''
	def __init__(self, slot, validator_index, h1_slot, h1_parent_root, h1_state_root, h1_body_root, h1_sign, h2_slot, h2_parent_root, h2_state_root, h2_body_root, h2_sign):
		self.slot = slot
		self.validator_index = validator_index
		self.h1_slot = h1_slot
		self.h1_parent_root = h1_parent_root
		self.h1_state_root = h1_state_root
		self.h1_body_root = h1_body_root
		self.h1_sign = h1_sign
		self.h2_slot = h2_slot
		self.h2_parent_root = h2_parent_root
		self.h2_state_root = h2_state_root
		self.h2_body_root = h2_body_root
		self.h2_sign = h2_sign

	
	
	
		
