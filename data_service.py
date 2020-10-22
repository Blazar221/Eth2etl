import pymysql
from encode import db_fit
from config import db


def attestation_insert(attestation_array):
	db = connect_db()
	sql_values = ""
	for item in attestation_array:
		sql_values = sql_values + "('{}', {}, {}, '{}', {}, '{}', {}, '{}', '{}'),".format(db_fit(item.aggr_bits), item.slot, item.cmt_index, db_fit(item.block_root), item.src_epoch, db_fit(item.src_block), item.trgt_epoch, db_fit(item.trgt_block), item.sign)
	sql = 'insert into attestation values {}'.format(sql_values)
	db.cursor().execute(sql[:-1]) # eliminate the last comma
	close_db(db)


def connect_db():
	return pymysql.connect(db['host'], db['user'], db['password'], db['name'])


def close_db(db):
	 db.close()
