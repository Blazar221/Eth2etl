#!/bin/bash
ACCOUNT='root'
PASSWORD='root'

echo 'hello linux!'
mysql -u ${ACCOUNT} -p${PASSWORD} -e "
	create database if not exists eth2data;
	use eth2data;
	create table if not exists attestation(
		aggregation_bits varchar(255) not null,
		slot int unsigned,
		committee_index mediumint unsigned,
		block_root char(44) not null,
		source_epoch int unsigned,
		source_root char(44) not null,
		target_epoch int unsigned,
		target_root char(44) not null,
		signature char(128))engine=myisam default charset=gbk;
"
