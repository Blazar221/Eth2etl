import pymysql
from encode import db_parse
from config import DB
# Each insertation needs the entity array as parameter, this way should avoid the frequent calling of the database connection.

def attestation_insert(attestation_array):
	sql_values = ""
	for item in attestation_array:
		sql_values = sql_values + "({}, '{}', {}, {}, '{}', {}, '{}', {}, '{}', '{}'),".format(item.inclusion_slot, item.aggr_bits, item.slot, item.cmt_index, item.block_root, item.src_epoch, item.src_block, item.trgt_epoch, item.trgt_block, item.sign)
	__insert_array('attestation', sql_values)


def attestation_query(**kwargs):
	return __query_all('attestation', **kwargs)


def block_insert(block_array):
	sql_values = ""
	for item in block_array:
		sql_values = sql_values + "({}, {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', {}, {}, {}, {}),".format(item.slot, item.prop_index, item.parent_root, item.state_root, item.randao_reveal, item.grff, item.sign, item.block_root, item.dpst_root, item.dpst_count, item.block_hash, item.has_dpst, item.has_exiting, item.has_sa, item.has_sp)
	__insert_array('block', sql_values)


def block_query(**kwargs):
	return __query_all('block', **kwargs)


def deposit_insert(deposit_array):
	sql_values = ""
	sql_proof_values = ""
	for item in deposit_array:
		sql_values = sql_values + "({}, '{}', '{}', '{}', {}, '{}'),".format(item.slot, item.block_root, item.pub_key, item.withdraw_cred, item.amount, item.sign)
		for each_proof in item.proof:
			sql_proof_values = sql_proof_values + "({}, '{}', '{}'),".format(item.slot, item.block_root, each_proof)
	__insert_array('deposit', sql_values)
	__insert_array('proof', sql_proof_values)


def deposit_query(**kwargs):
	data = __query_all('deposit', **kwargs)
	proof_data = []
	for each in data:
		proof_data.append(__query_all('proof', slot = each[0], block_root = each[1]))
	return data, proof_data


def exiting_insert(ex_array):
	sql_values = ""
	for item in ex_array:
		sql_values = sql_values + "({}, '{}', {}, {}, '{}'),".format(item.slot, item.block_root, item.exit_epoch, item.vld_index, item.sign)
	__insert_array('slashingp', sql_values)


def slashinga_insert(sa_array):
	sql_values = ""
	sql_vld_values = ""
	for item in sa_array:
		sql_values = sql_values + "({}, '{}', {}, {}, '{}', {}, '{}', {}, '{}', '{}',{}, {}, '{}', {}, '{}', {}, '{}', '{}'),".format(item.slot, item.block_root, item.slot1, item.cmt_index1, item.block_root1, item.src_epoch1, item.src_root1, item.trgt_epoch1, item.trgt_root1, item.sign1, item.slot2, item.cmt_index2, item.block_root2, item.src_epoch2, item.src_root2, item.trgt_epoch2, item.trgt_root2, item.sign2)
		for each_vld in item.indice1:
			sql_vld_values = sql_vld_values + "({}, '{}', {}, {}),".format(item.slot, item.block_root, each_vld, True)
		for each_vld in item.indice2:
			sql_vld_values = sql_vld_values + "({}, '{}', {}, {}),".format(item.slot, item.block_root, each_vld, False)
	__insert_array('slashinga', sql_values)
	__insert_array('slashinga_vld', sql_vld_values)


def slashinga_query(**kwargs):
	data = __query_all('slashinga', **kwargs)
	vld_data = []
	for each in data:
		vld_data.append(__query_all('slashinga_vld', slot = each[0], block_root = each[1]))
	return data, vld_data


def slashingp_insert(sp_array):
	sql_values = ""
	for item in sp_array:
		sql_values = sql_values + "({}, '{}', {}, {}, '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}'),".format(item.slot, item.block_root, item.vld_index, item.slot1, item.parent_root1, item.state_root1, item.body_root1, item.sign1, item.slot2, item.parent_root2, item.state_root2, item.body_root2, item.sign2)
	__insert_array('slashingp', sql_values)


def slashingp_query(**kwargs):
	return __query_all('slashingp', **kwargs)


def validator_insert(vld_array):
	sql_values = ""
	for item in vld_array:
		sql_values = sql_values + "({}, '{}', '{}', {}, {}, '{}', '{}', '{}', '{}'),".format(item.index, item.pub_key, item.withdraw_cred, item.e_balance, item.slashed, item.act_eli_epoch, item.act_epoch, item.exit_epoch, item.withdraw_epoch)
	__insert_array('validator', sql_values)


def validator_query(**kwargs):
	return __query_all('validator', **kwargs)


def __insert_array(table, sql_values):
	sql = 'insert into {} values {}'.format(table, sql_values)
	if sql[-1] == ',': # If exists, eliminate the last comma
		sql = sql[:-1]
	db = __connect_db()
	db.cursor().execute(sql)
	db.close()


def __query_all(table, **kwargs):
	sql = 'select * from {}'.format(table)
	if kwargs:
		sql_values = ''
		for key in kwargs.keys():
			if kwargs[key] is not None: # The parameter shouldn't be none
				value = kwargs[key]
				if type(value) == type('a') and len(value) > 0: # String parameter need quotation
					sql_values = sql_values + " {}='{}' and".format(key, kwargs[key])
				else:
					sql_values = sql_values + " {}={} and".format(key, kwargs[key])
		if sql_values:
					sql = sql + ' where' + sql_values[:-3]
	print(sql)
	db = __connect_db()
	cursor = db.cursor()
	cursor.execute(sql)
	res = cursor.fetchall()
	db.close()
	return res


def __connect_db():
	return pymysql.connect(DB['HOST'], DB['USER'], DB['PASSWORD'], DB['NAME'])


