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

		
