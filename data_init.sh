#!/bin/bash
#This script can only work after running data_init first
ACCOUNT='root'
PASSWORD='root'

echo 'hello linux!'
mysql -u ${ACCOUNT} -p${PASSWORD} -e "
	create database if not exists eth2data;
	use eth2data;
	create table if not exists attestation(
		inclusion_slot int unsigned,
		aggr_bits varchar(255) not null,
		slot int unsigned,
		cmt_index mediumint unsigned,
		block_root char(43) not null,
		src_epoch mediumint unsigned,
		src_root char(43) not null,
		trgt_epoch mediumint unsigned,
		trgt_root char(43) not null,
		sign char(128))engine=myisam default charset=gbk;
	create table if not exists block(
		slot int unsigned,
		prop_index mediumint unsigned,
		parent_root char(43) not null,
		state_root char(43) not null,
		randao_reveal char(128) not null,
		grff char(43) not null,
		sign char(128) not null,
		block_root char(43) not null,
		dpst_root char(43) not null,
		dpst_count int unsigned,
		block_hash char(43) not null,
		has_dpst boolean,
		has_exit boolean,
		has_sa boolean,
		has_sp boolean)engine=myisam default charset=gbk;
	create table if not exists deposit(
		slot int unsigned,
		block_root char(43) not null,
		pub_key char(64) not null,
		withdraw_cred char(43) not null,
		amount tinyint,
		sign char(128) not null)engine=myisam default charset=gbk;
	create table if not exists proof(
		slot int unsigned,
		block_root char(43) not null,
		value char(43) not null)engine=myisam default charset=gbk;		
	create table if not exists slashinga(
		slot int unsigned,
		block_root char(43) not null,
		slot1 int unsigned,
		cmt_index1 mediumint unsigned,
		block_root1 char(43) not null,
		src_epoch1 mediumint unsigned,
		src_root1 char(43) not null,
		trgt_epoch1 mediumint unsigned,
		trgt_root1 char(43) not null,
		sign1 char(128) not null,
		slot2 int unsigned,
		cmt_index2 mediumint unsigned,
		block_root2 char(43) not null,
		src_epoch2 mediumint unsigned,
		src_root2 char(43) not null,
		trgt_epoch2 mediumint unsigned,
		trgt_root2 char(43) not null,
		sign2 char(128) not null)engine=myisam default charset=gbk;
	create table if not exists slashinga_vld(
		slot int unsigned,
		block_root char(43) not null,
		vld_index mediumint unsigned,
		first boolean)engine=myisam default charset=gbk;
	create table if not exists slashingp(
		slot int unsigned,
		block_root char(43) not null,
		vld_index mediumint unsigned,
		slot1 int unsigned,
		parent_root1 char(43) not null,
		state_root1 char(43) not null,
		body_root1 char(43) not null,
		sign1 char(128) not null,
		slot2 int unsigned,
		parent_root2 char(43) not null,
		state_root2 char(43) not null,
		body_root2 char(43) not null,
		sign2 char(128) not null)engine=myisam default charset=gbk;	
	create table if not exists validator(
		id mediumint unsigned,
		pub_key char(64) not null,
		withdraw_cred char(43) not null,
		e_balance tinyint,
		slashed boolean,
		act_eli_epoch mediumint unsigned,
		act_epoch mediumint unsigned,
		exit_epoch mediumint unsigned,
		withdraw_epoch mediumint unsigned,
		primary key (id))engine=myisam default charset=gbk;			
"
