#!usr/bin/python3
import api_service
import base_service
import data_service

if __name__ == '__main__':
	print('begin')
	raw_data = api_service.attestations_epoch(2, pageSize = 2)
	attestation_array = base_service.json_to_attestation_array(raw_data)	
	for each in attestation_array:
		print(each)
	data_service.attestation_insert(attestation_array)
	print('end')

