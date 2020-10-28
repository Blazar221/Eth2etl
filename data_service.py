import pymysql
from encode import db_parse
from config import db
# Each insertation needs the entity array as parameter, this way should avoid the frequent calling of the database connection.

def attestation_insert(attestation_array):
	sql_values = ""
	for item in attestation_array:
		sql_values = sql_values + "('{}', {}, {}, '{}', {}, '{}', {}, '{}', '{}'),".format(db_parse(item.aggr_bits), item.slot, item.cmt_index, db_parse(item.block_root), item.src_epoch, db_parse(item.src_block), item.trgt_epoch, db_parse(item.trgt_block), item.sign)
	sql = 'insert into attestation values {}'.format(sql_values)
	insert_array('attestation', sql_values)


def deposit_insert(deposit_array):
	sql_values = ""
	for item in deposit_array:
		sql_values = sql_values + "({}, '{}', '{}', '{}', {}, '{}'),".format(item.slot, db_parse(item.block_root), item.pub_key, db_parse(item.withdraw_cred), item.amount, item.sign)
	insert_array('deposit', sql_values)


def proof_insert(proof_array):
	sql_values = ""
	for item in proof_array:
		sql_values = sql_values + "({}, '{}', '{}')".format(item.slot, db_parse(item.block_root), db_parse(item.value))
	insert_array('proof', sql_values)


def insert_array(table, sql_values):
	sql = 'insert into {} values {}'.format(table, sql_values)
	if sql[-1] == ',': # If exists, eliminate the last comma
		sql = sql[:-1]
	db = connect_db()
	db.cursor().execute(sql)
	db.close()


def connect_db():
	return pymysql.connect(db['host'], db['user'], db['password'], db['name'])


