from utils import time_util
from constant import SLOT_PER_EPOCH


class attestation:
    def __init__(self, inclusion_slot, aggr_bits, slot, cmt_index, block_root, src_epoch, src_block, trgt_epoch,
                 trgt_block, sign):
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
        return 'inclusion={}, aggr_bits={}, slot={}, cmt_index={}, block_root={}, src_epoch={}, src_root={}, trgt_epoch={}, trgt_root={}, sign={}'.format(
            self.inclusion_slot, self.aggr_bits, self.slot, self.cmt_index, self.block_root, self.src_epoch,
            self.src_block, self.trgt_epoch, self.trgt_block, self.sign)

    def csv_line(self):
        return (
            self.aggr_bits, self.slot, self.cmt_index, self.block_root, self.src_epoch, self.src_block, self.trgt_epoch,
            self.trgt_block, self.sign)


class deposit:
    def __init__(self, block_root, proof, pub_key, withdraw_cred, amount, sign):
        self.block_root = block_root
        self.proof = proof
        self.pub_key = pub_key
        self.withdraw_cred = withdraw_cred
        self.amount = amount
        self.sign = sign

    def __repr__(self):
        return 'block_root={},proof={},pub_key={},withdraw_cred={},amount={},sign={}'.format(self.block_root,
                                                                                             self.proof, self.pub_key,
                                                                                             self.withdraw_cred,
                                                                                             self.amount, self.sign)

    def csv_line(self):
        return (self.pub_key, self.withdraw_cred, self.amount, self.sign)


class exiting:
    def __init__(self, block_root, exit_epoch, vld_index, sign):
        self.block_root = block_root
        self.exit_epoch = exit_epoch
        self.vld_index = vld_index
        self.sign = sign

    def __repr__(self):
        return 'block_root={},exit_epoch={},validator_index={},sign={}'.format(self.block_root, self.exit_epoch,
                                                                               self.validator_index, self.sign)

    def csv_line(self):
        return (self.exit_epoch, self.validator_index, self.sign)


class slashinga:
    def __init__(self, block_root, indice1, slot1, cmt_index1, block_root1, src_epoch1, src_root1, trgt_epoch1,
                 trgt_root1, sign1, indice2, slot2, cmt_index2, block_root2, src_epoch2, src_root2, trgt_epoch2,
                 trgt_root2, sign2):
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
        return 'block_root={},indice1={},slot1={}, cmt_index1={},block_root1={},src_epoch1={},src_root1={},trgt_epoch1={},trgt_root1={},sign1={},indice2={},slot2={}, cmt_index2={},block_root2={},src_epoch2={},src_root2={},trgt_epoch2={},trgt_root2={},sign2={}'.format(
            self.block_root, self.indice1, self.slot1, self.cmt_index1, self.block_root1, self.src_epoch1,
            self.src_root1, self.trgt_epoch1, self.trgt_root1, self.sign1, self.indice2, self.slot2, self.cmt_index2,
            self.block_root2, self.src_epoch2, self.src_root2, self.trgt_epoch2, self.trgt_root2, self.sign2)

    def csv_line(self):
        return (
            *self.indice1, self.slot1, self.cmt_index1, self.block_root1, self.src_epoch1, self.src_root1,
            self.trgt_epoch1,
            self.trgt_root1, self.sign1, *self.indice2, self.slot2, self.cmt_index2, self.block_root2, self.src_epoch2,
            self.src_root2, self.trgt_epoch2, self.trgt_root2, self.sign2)


class slashingp:
    def __init__(self, block_root, vld1, slot1, parent_root1, state_root1, body_root1, sign1, vld2, slot2, parent_root2,
                 state_root2, body_root2, sign2):
        self.block_root = block_root
        self.vld1 = vld1
        self.vld2 = vld2
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

    def csv_line(self):
        return (
            self.slot1, self.vld1, self.parent_root1, self.state_root1, self.body_root1, self.sign1, self.slot2,
            self.vld2,
            self.parent_root2, self.state_root2, self.body_root2, self.sign2)


class validator:
    def __init__(self, index, pub_key, withdraw_cred, e_balance, slashed, act_eli_epoch, act_epoch, exit_epoch,
                 withdraw_epoch):
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
        return 'index={},pub_key={},withdraw_cred={},e_balance={},slashed={},act_eli_epoch={},act_epoch={},exit_epoch={},withdraw_epoch={}'.format(
            self.index, self.pub_key, self.withdraw_cred, self.e_balance, self.slashed, self.act_eli_epoch,
            self.act_epoch, self.exit_epoch, self.withdraw_epoch)

    def line(self):
        return (
            self.index, self.pub_key, self.withdraw_cred, self.e_balance, self.slashed, self.act_eli_epoch,
            self.act_epoch,
            self.exit_epoch, self.withdraw_epoch)


class committee:
    def __init__(self, slot, index, indices):
        self.slot = int(slot)
        self.index = index
        self.indices = indices

    def csv_line(self):
        epoch = int(self.slot / SLOT_PER_EPOCH)
        return (epoch, time_util.get_timestamp_epoch(epoch), self.slot, self.index, *self.indices)
