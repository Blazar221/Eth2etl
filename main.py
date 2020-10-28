#!usr/bin/python3
import api_service
import base_service
import data_service


if __name__ == '__main__':
	print('begin')
	for epoch_value in range(0, 1):
		raw_data = api_service.block_epoch(epoch_value)
		res = base_service.json_to_block_array(raw_data)
		for each in res: 
			block, deposit, exit, sa, ss = each
			print(block)				
	print('end')

