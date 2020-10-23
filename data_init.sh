#!/bin/bash
ACCOUNT='root'
PASSWORD='root'

echo 'hello linux!'
mysql -u ${ACCOUNT} -p${PASSWORD} -e "
	create database if not exists eth2data;
	use eth2data;
	create table if not exists attestation(
		aggr_bits varchar(255) not null,
		slot int unsigned,
		cmt_index mediumint unsigned,
		block_root char(43) not null,
		src_epoch mediumint unsigned,
		src_root char(43) not null,
		trgt_epoch mediumint unsigned,
		trgt_root char(43) not null,
		sign char(128))engine=myisam default charset=gbk;
	create table if not exists slashinga(
		slot int unsigned,
		a1_indice mediumint unsigend,
		a1_slot int unsigned,
		a1_cmt_index mediumint unsigned,
		a1_block_root char(43) not null,
		a1_src_epoch mediumint unsigned,
		a1_src_root char(43) not null,
		a1_trgt_epoch mediumint unsigned,
		a1_trgt_root char(43) not null,
		a1_sign char(128) not null,
		a2_indice mediumint unsigend,
		a2_slot int unsigned,
		a2_cmt_index mediumint unsigned,
		a2_block_root char(43) not null,
		a2_src_epoch mediumint unsigned,
		a2_src_root char(43) not null,
		a2_trgt_epoch mediumint unsigned,
		a2_trgt_root char(43) not null,
		a2_sign char(128) not null)engine=myisam default charset=gbk;
	create table if not exists slashingp(
		slot int unsigned,
		validator_index mediumint unsigned,
		h1_slot int unsigned,
		h1_parent_root char(43) not null,
		h1_state_root char(43) not null,
		h1_body_root char(43) not null,
		h1_sign char(128) not null,
		h2_slot int unsigned,
		h2_parent_root char(43) not null,
		h2_state_root char(43) not null,
		h2_body_root char(43) not null,
		h2_sign char(128) not null)engine=myisam default charset=gbk;		
"
