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
		indice1 mediumint unsigend,
		slot1 int unsigned,
		cmt_index1 mediumint unsigned,
		block_root1 char(43) not null,
		src_epoch1 mediumint unsigned,
		src_root1 char(43) not null,
		trgt_epoch1 mediumint unsigned,
		trgt_root1 char(43) not null,
		sign1 char(128) not null,
		indice2 mediumint unsigend,
		slot2 int unsigned,
		cmt_index2 mediumint unsigned,
		block_root2 char(43) not null,
		src_epoch2 mediumint unsigned,
		src_root2 char(43) not null,
		trgt_epoch2 mediumint unsigned,
		trgt_root2 char(43) not null,
		sign2 char(128) not null)engine=myisam default charset=gbk;
	create table if not exists slashingp(
		slot int unsigned,
		slot1 int unsigned,
		index1 mediumint unsigned,
		parent_root1 char(43) not null,
		state_root1 char(43) not null,
		body_root1 char(43) not null,
		sign1 char(128) not null,
		slot2 int unsigned,
		index2 mediumint unsigned,
		parent_root2 char(43) not null,
		state_root2 char(43) not null,
		body_root2 char(43) not null,
		sign2 char(128) not null)engine=myisam default charset=gbk;		
"
